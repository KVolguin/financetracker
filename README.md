# **Expense Tracker Web App**
#### Video Demo:  https://youtu.be/MOmq5x5MRu8
#### Description:
I created an expense tracker using **Flask**, **Django/Jinja**, and **SQLite**. I created my own development environemnt in Windows using WSL, and used git for version control and github as a backup. I used werkzeug for password/username hashing and security. I used chart.js for making charts. It's a very simple app, it just allows a user to make an account, add their expenses with a description, category, and date, and do some basic things with the data. Users can filter the data thats been entered, export it as a CSV, and view a couple of helpful graphs that show a pie chart and a line graph of their expenses over time. I wanted to create this app to further practice understanding and using Flask and HTML/CSS, as well as handling all the files needed for it. I also wanted to do a project that was relatively simple so that I could focus more on using my own IDE and git/github without the complications that come with overreaching my capabilities and, frankly, time I have left to build this project due to feature creep. Feature creep was a major issue in my last project and it took 3 times longer than I first anticipated. By keeping the scope relatively shallow I was able to complete something within a much more reasonable amount of time.

Below are listed out all the features in more detail.
#### github link https://github.com/KVolguin/financetracker
---

## **Features**

### **1. User Authentication**
- **Register** Lets you create a new account with a unique username and password.
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
- View filtered results after pressing "filter"

### **4. Data Export**
- Export/download all expenses as a **CSV file** for further use.

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
│   ├── home.html        # Home page with basic instructions of how to use the site
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
```

# **User flow with screenshots**


![A user is brought to the normal home site upon opening. ](https://ucf5eac8ec9c44c8b87339953041.previews.dropboxusercontent.com/p/thumb/ACeypnqr2z1js4s_xnFoGJKnrXX_Y58KU9A5Twnob9GRcQ31hexOfqXnvxiKAQD9oGcpWFYyViC-NfNfQaIuzoJCYjEZHMbK0ULEKEjRs-3t0wj8Sp0XDjMGzSyhpXIfkSmGXZqA8VNgn_-Jh_x6hmGtIlRxQkdVSgZpLPK_akRUPjXwxz73cUvhZKkqsgNBepcaEqCG0YUeBLM9NZxV1BTjx8rsLt0SVElo4sk80R2soSSE_-88wimh8rrLtgqWIgbmPKO8fs_Ec2Vqx7MmYxPIykcmKjmy6UxUCxFU0X8bTME8d-hemJHqg1Qz-ghGdlgAgourGmm-FTULod9cAMHTE5pe3DxTq1ThDnlUGeTBRSRr_uwVF3rIzo3idTQH5xw/p.png?is_prewarmed=true)

### A user is brought to the home site upon opening. 
### They then should see the navbar which says "Home", "Register" and "Login", and nothing else.


![Register](https://dl.dropbox.com/scl/fi/16hfwxao9rpq424evj65r/2-register.PNG?rlkey=bslsw23ieisjionz71pvdygln&e=1&dl=0)

### Naturally, hopefully, they should decide to register. Its extremely simple, but it works and is hashed for security.

![login](https://dl.dropboxusercontent.com/scl/fi/w73lpd50wlp57ckbqn84l/3-login.PNG?rlkey=kcwkuoptk68tb7r57yowd6h54&e=1&dl=0)
### After registration they're automatically brought to the login page where their browser should automatically have input their
### login data. Clicking login logs them in and brings them to the View Expenses page

![View Expenses](https://dl.dropbox.com/scl/fi/ubb18fnatq5w9zw6613y7/4-view-expenses.PNG?rlkey=6i57h60uv45r5rp1r12kyyjm6&e=1&dl=0)
### This allows the user to see all their expenses, with their ID (just sequentially made), description, expense, date, and actions.
### Users can edit and delete each item. 

![Edit Expenses](https://dl.dropbox.com/scl/fi/or423507brb17nxzwiccu/4-5-edit-expense.PNG?rlkey=fmlx1eiq4t8y5lmvzg0apune6&e=1&dl=0)
### Here a user can edit previously entered expenses if an error was made

![Add Expenses](https://dl.dropbox.com/scl/fi/4zj71exuxi5l3goix22f8/5-add-expenses.PNG?rlkey=e7vqjqqi0eg3xrtodwfvgxz4i&e=1&dl=0)
### Users can enter in each category to add an expense. It wont let you add one unless you fill in all fields.

[Category Dropdown](https://dl.dropbox.com/scl/fi/3gwo2ramvp6h757d5kfmy/5-5-dropdown.PNG?rlkey=i6uoxbrx7tgjxpdee92csw89j&e=1&dl=0)
### Users can take advantage of having their previous categories they've entered show up during the adding process to prevent any
### slightly-off duplicate categories from being made or forgetting past ones.

![Expense Dashboard](https://dl.dropbox.com/scl/fi/ps9qs66wjnyfkbwj1j2fa/6-expense-dashboard.PNG?rlkey=4z0jt8vxp0cfp89is9m45clls&e=1&dl=0)
### A semi-interactive dashboard that shows expenses in a graphical format.
### Pie chart shows expenses by category, and hovering shows how much is in each piece of pie.

![Filter by Category, Date](https://dl.dropbox.com/scl/fi/gtu4lx1j6vr0ouww3fb72/7-Filter-by-category-date.PNG?rlkey=niu3ppcezf2zwg9xcwkv29mio&e=1&dl=0)
### Very handy feature to filter expenses by category and the date that it was entered.

![Export data as CSV](https://dl.dropbox.com/scl/fi/md2cghyr1s4ntbg2i2ja0/8-Export-data-as-CSV.PNG?rlkey=8sznbq1ohu5si5sfmq2i171sn&e=2&dl=0)
### Another very handy feature which lets users export their entries as a CSV, allowing them to take full advantage of other more powerful tools to analyze their data whatever way they wish.

![Exported data opened in Excel](https://dl.dropbox.com/scl/fi/k9e4pjmfuldunqjm2243j/9-exported-CSV-data-in-excel.PNG?rlkey=dg6lf0iqtumovy4g6mqw463u7&e=1&dl=0L)
### An example of data exported in excel. It actually didn't look this clean when entered, future revisions will need to include characters not allowed in data entry.
### There was a slash between shocks/wheels which split the entry into more columns for that row.

![Logging out shows Logout message; these confirmation messages are present throughout the app](https://dl.dropbox.com/scl/fi/3luz342p4fup2hq7x37dj/10-Logging-out-shows-message.PNG?rlkey=vatobea8z809tc34rzr9ydnsc&e=1&dl=0)
### Logging out shows a confirmation message that you've done so, and these types of messages also appear when an expense is added, edited, deleted successfully.

![Flexbox is used throughout the site to make elements responsive when viewed on smaller screens](https://dl.dropbox.com/scl/fi/n3dp3vu47myu043d27bs2/11-Using-flexbox-responsive.PNG?rlkey=vx59nyd5xchc233m6o7if1uay&e=1&dl=0)
### I used flexbox for the CSS and layout to ensure that elements stay responsive even when viewed on smaller screens or screens with different proportions.

![Some pages need work but are still functional](https://dl.dropbox.com/scl/fi/dm5rgwr35xbtmoe4ke6jt/12-Some-pages-need-work-but-are-functional.PNG?rlkey=j3zilzq9mfyyd80r331p31edj&e=1&dl=0)
### Some pages would probably need to be reconfigured for mobile but are still fully functional despite the uglyness.

## Future additions
If I had the time I'd have liked to add:
- regex what characters are allowed on input
- more ways to filter data, like data range, includes a b c or partial words
- a "today" button for date, or set automatically to "today" when adding an expense
- recurring expenses feature
- many, many more styles and types of graphs
- whether youv'e gone over or under budget for the current week, month, year
- a way to import data from another CSV
- visualizing multiple months onto each other in a area graph to see your overall progress in 3 dimensions
- Prettying up and tidying user experience; a lot of pages are adjusted completely to the left
- introducing hotkeys for super fast data input and moving between tabs
- personalizing the Home screen with at least "Hello, (username)", or "register an account" if not logged in
- have a "overall health" score for your homepage
- Create automated tips for what categories could be reduced

## Contributors
This project was developed with the guidance of ChatGPT and learning from Flask, HTML, CSS, and SQLite.

## License
This project is licensed under the MIT License.

---

### Key Notes:
1. **Markdown Ready**: This document uses proper headings, bold text, tables, and code blocks for easy readability in any Markdown viewer (e.g., GitHub, VSCode).
2. **Comprehensive**: Includes setup instructions, features, database structure, and file organization.
3. **Polished**: Future improvements and visual details are included.

### Contact Info
email: kvolguin@gmail.com