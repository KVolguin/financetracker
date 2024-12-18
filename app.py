from flask import Flask, request, render_template, redirect, flash, session, Response
import csv
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = 'whatever'

# Initialize the database
def init_db():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            description TEXT NOT NULL,
            category TEXT,
            date TEXT,
            user_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    conn.commit()
    conn.close()


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
    if 'user_id' not in session:
        flash('Please log in to add expenses.')
        return redirect('/login')

    user_id = session['user_id']
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()

    categories = [] 

    try:
        # Fetch unique categories for the user
        cursor.execute('SELECT DISTINCT category FROM expenses WHERE user_id = ? AND category IS NOT NULL', (user_id,))
        categories = [row[0] for row in cursor.fetchall()]

        if request.method == 'POST':
            amount = request.form.get('amount')
            description = request.form.get('description')
            category = request.form.get('category')
            date = request.form.get('date')

            cursor.execute('BEGIN')

            cursor.execute('INSERT OR IGNORE INTO user_counters (user_id, last_expense_id) VALUES (?, ?)', (user_id, 0))

            cursor.execute('SELECT last_expense_id FROM user_counters WHERE user_id = ?', (user_id,))
            result = cursor.fetchone()
            new_expense_id = (result[0] if result else 0) + 1

            cursor.execute('''
                INSERT INTO expenses (id, user_id, amount, description, category, date)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (new_expense_id, user_id, amount, description, category, date))

            cursor.execute('UPDATE user_counters SET last_expense_id = ? WHERE user_id = ?', (new_expense_id, user_id))

            conn.commit()
            flash('Expense added successfully!')
            return redirect('/view')

    except sqlite3.Error as e:
        conn.rollback()
        flash(f'An error occurred: {str(e)}')

    finally:
        conn.close()

    return render_template('add.html', categories=categories)





@app.route('/view', methods=['GET'])
def view():
    if 'user_id' not in session:
        flash('Please log in to view your expenses.')
        return redirect('/login')
    
    user_id = session['user_id']
    category = request.args.get('category')
    date = request.args.get('date')

    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()

    query = 'SELECT id, amount, description, category, date FROM expenses WHERE user_id = ?'
    params = [user_id]

    if category:
        query += ' AND category = ?'
        params.append(category)

    if date:
        query += ' AND date = ?'
        params.append(date)

    cursor.execute(query, params)
    expenses = cursor.fetchall()

    cursor.execute('SELECT SUM(amount) FROM expenses WHERE user_id = ?', (user_id,))
    total = cursor.fetchone()[0] or 0

    conn.close()
    return render_template('view.html', expenses=expenses, total=round(total, 2))


@app.route('/edit/<int:expense_id>', methods=['GET', 'POST'])
def edit(expense_id):
    if 'user_id' not in session:
        flash('Please log in to edit expenses.')
        return redirect('/login')

    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()

    if request.method == 'POST':
        amount = request.form.get('amount')
        description = request.form.get('description')
        category = request.form.get('category')
        date = request.form.get('date')

        cursor.execute('UPDATE expenses SET amount = ?, description = ?, category = ?, date = ? WHERE id = ?', 
                       (amount, description, category, date, expense_id))
        conn.commit()
        conn.close()
        flash('Expense updated successfully!')
        return redirect('/view')
    
    cursor.execute('SELECT amount, description, category, date FROM expenses WHERE id = ?', (expense_id,))
    expense = cursor.fetchone()
    conn.close()

    return render_template('edit.html', expense_id=expense_id, expense=expense)


@app.route('/delete/<int:expense_id>', methods=['POST'])
def delete(expense_id):
    if 'user_id' not in session:
        flash('Please log in to delete expenses.')
        return redirect('/login')

    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))
    conn.commit()
    conn.close()
    flash('Expense deleted successfully!')
    return redirect('/view')


@app.route("/export", methods=['GET'])
def export():
    if 'user_id' not in session:
        flash('Please log in to export expenses.')
        return redirect('/login')
    
    user_id = session['user_id']
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, amount, description, category, date FROM expenses WHERE user_id = ?', (user_id,))
    expenses = cursor.fetchall()
    conn.close()

    def generate():
        yield ','.join(['ID', 'Amount', 'Description', 'Category', 'Date']) + '\n'
        for expense in expenses:
            yield ','.join(map(str, expense)) + '\n'
    
    return Response(generate(), mimetype='text/csv', headers={
        'Content-Disposition': 'attachment; filename=expenses.csv'
    })


@app.route('/dashboard', methods=['GET'])
def dashboard():
    if 'user_id' not in session:
        flash('Please log in to view the dashboard.')
        return redirect('/login')

    user_id = session['user_id']

    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('SELECT category, SUM(amount) FROM expenses WHERE user_id = ? GROUP BY category', (user_id,))
    category_data = cursor.fetchall()
    cursor.execute('SELECT date, SUM(amount) FROM expenses WHERE user_id = ? GROUP BY date ORDER BY date', (user_id,))
    date_data = cursor.fetchall()
    conn.close()

    return render_template('dashboard.html', category_data=category_data, date_data=date_data)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        conn = sqlite3.connect('expenses.db')
        cursor = conn.cursor()

        try:
            cursor.execute('INSERT INTO users (username, password) VALUES(?, ?)', (username, hashed_password))
            conn.commit()
            flash('Account created successfully! Please log in.')
            return redirect('/login')
        except sqlite3.IntegrityError:
            flash('Username already exists. Try a different one.')
        finally:
            conn.close()

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('expenses.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, password FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user[1], password):
            session['user_id'] = user[0]
            flash('Login successful!')
            return redirect('/view')
        else:
            flash('Invalid username or password.')
        
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Logged out successfully.')
    return redirect('/login')

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
