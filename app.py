from flask import Flask, request, render_template, redirect, flash, session, Response
import csv

import sqlite3

app = Flask(__name__)
app.secret_key = 'whatever'

# Initialize the database
def init_db():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            description TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        amount = request.form.get('amount')
        description = request.form.get('description')
        category = request.form.get('category')
        date = request.form.get('date')

        # Save the data to the database
        conn = sqlite3.connect('expenses.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO expenses (amount, description, category, date) VALUES (?, ?, ?, ?)',
                        (amount, description, category, date))
        conn.commit()
        conn.close()

        flash('Expense added successfully!')
        return redirect('/view')

    
    # Render the form using the add.html template
    return render_template('add.html')

@app.route('/view', methods=['GET'])
def view():
    category = request.args.get('category')
    date = request.args.get('date')

    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()

    # Fetch all columns, includign category and date
    query = 'SELECT id, amount, description, category, date FROM expenses'
    params = []

    if category:
        query += ' WHERE category = ?'
        params.append(category)

    if date:
        query += ' AND date = ?' if 'WHERE' in query else ' WHERE date = ?'
        params.append(date)

    cursor.execute(query, params)
    expenses = cursor.fetchall()

    # Calculate total expenses
    cursor.execute('SELECT SUM(amount) FROM expenses' + (' WHERE category = ?' if category else '') + (' AND date = ?' if date else ''), params)
    total = cursor.fetchone()[0] or 0

    conn.close()

    return render_template('view.html', expenses=expenses, total=round(total, 2))

@app.route('/edit/<int:expense_id>', methods=['GET', 'POST'])
def edit(expense_id):
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()

    if request.method == 'POST':
        # Update the expense in the database
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
    
    # Fetch the current expense details
    cursor.execute('SELECT amount, description, category, date FROM expenses WHERE id = ?', (expense_id,))
    expense = cursor.fetchone()
    conn.close()

    return render_template('edit.html', expense_id=expense_id, expense=expense)

@app.route('/delete/<int:expense_id>', methods=['POST'])
def delete(expense_id):
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))
    conn.commit()
    conn.close()
    flash('Expense deleted successfully!')
    return redirect('/view')

@app.route("/export", methods=['GET'])
def export():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, amount, description, category, date FROM expenses')
    expenses = cursor.fetchall()
    conn.close()

    # Create CSV response
    def generate():
        # Write CSV header
        yield ','.join(['ID', 'Amount', 'Description', 'Category', 'Date']) + '\n'
        # Write each expense as a CSV row
        for expense in expenses:
            yield ','.join(map(str, expense)) + '\n'
    
    return Response(generate(), mimetype='text/csv', headers = {
        'Content-Disposition': 'attachment; filename=expenses.csv'
    })


@app.route('/dashboard', methods=(['GET']))
def dashboard():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()

    # Fetch data for visualizations
    cursor.execute('SELECT category, SUM(amount) FROM expenses GROUP BY category')
    category_data = cursor.fetchall()

    cursor.execute('SELECT date, SUM(amount) FROM expenses GROUP BY date ORDER BY date')
    date_data = cursor.fetchall()
    conn.close()

    # Pass data to template
    return render_template('dashboard.html', category_data=category_data, date_data=date_data)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
