from flask import Flask, request, render_template, redirect
import sqlite3

app = Flask(__name__)

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

        # Save the data to the database
        conn = sqlite3.connect('expenses.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO expenses (amount, description) VALUES (?, ?)', (amount, description))
        conn.commit()
        conn.close()

        return 'Expense added successfully!'
    
    # Render the form using the add.html template
    return render_template('add.html')

@app.route('/view', methods=['GET'])
def view():
    # Connect to the database and retrieve all expenses
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()

    # Fetch expense records
    cursor.execute('SELECT id, amount, description FROM expenses')
    expenses = cursor.fetchall()  # List of tuples (id, amount, description)

    # Calculate total expenses
    cursor.execute('SELECT SUM(amount) FROM expenses')
    total = cursor.fetchone()[0] # Fetch total amount (return None if no rows yet)

    conn.close()

    # Round total to 2 decimal places
    total = round(total or 0, 2)

    # Render the expenses in the view.html template
    return render_template('view.html', expenses=expenses, total=total or 0)

@app.route('/edit/<int:expense_id>', methods=['GET', 'POST'])
def edit(expense_id):
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()

    if request.method == 'POST':
        # Update the expense in the database
        amount = request.form.get('amount')
        description = request.form.get('description')
        cursor.execute('UPDATE expenses SET amount = ?, description = ? WHERE id = ?', (amount, description, expense_id))
        conn.commit()
        conn.close()
        return redirect('/view')
    
    # Fetch the current expense details
    cursor.execute('SELECT amount, description FROM expenses WHERE id = ?', (expense_id,))
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
    return redirect('/view')


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
