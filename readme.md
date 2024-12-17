# **Expense Tracker Web Application**

This is a web-based expense tracking application built using **Flask** and **SQLite**. It allows users to securely log in, track expenses, filter entries, view data visualizations, and export expenses to a CSV file.

---

## **Features**

### **1. User Authentication**
- **Register** a new account with a unique username and password.
- **Login** to access personalized expense data.
- **Logout** securely from the application.

### **2. Expense Management**
- Add expenses with the following details:
  - Amount
  - Description
  - Category (auto-suggest from previous entries)
  - Date
- Edit or delete previously entered expenses.

### **3. Filter Expenses**
- Filter expenses based on:
  - **Category**
  - **Date**
- View filtered results dynamically in a table format.

### **4. Data Export**
- Export all expenses as a **CSV file** for further use.

### **5. Data Visualizations**
- A **Pie Chart** showing expenses grouped by category.
- A **Line Chart** showing expenses over time.

### **6. Dashboard**
- Displays interactive graphs for insights into spending habits.

### **7. Responsive UI**
- Forms and tables align neatly for a clean, professional user experience.
- Navbar highlights the current active page for better navigation.

---

## **Tech Stack**
- **Backend**: Flask (Python)
- **Database**: SQLite
- **Frontend**: HTML, CSS (Flexbox for layout)
- **Data Visualization**: Chart.js
- **Security**: Password hashing using Werkzeug

---

## **Project Structure**

```plaintext
project-folder/
│
├── app.py               # Main Flask application
├── expenses.db          # SQLite database file
├── templates/           # HTML templates
│   ├── base.html        # Base template with navbar
│   ├── home.html        # Home page
│   ├── add.html         # Add expense form
│   ├── view.html        # View expenses page
│   ├── edit.html        # Edit expense form
│   └── dashboard.html   # Dashboard with visualizations
│
├── static/              # Static files (CSS, JS, images)
│   ├── style.css        # CSS styles
│   └── Chart.js         # JavaScript library for charts
│
└── README.md            # Documentation
