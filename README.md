# Expense Tracker Web App

A Flask-based web application to track daily expenses and visualize summary data.

## Features
- Add expense with category, date, and amount
- View all expenses in a styled table
- Summary by category, date, and total
- Dark/Light mode switch
- CSV-based storage

## Technologies Used
- Python 3
- Flask
- HTML + Jinja2
- CSS with theme support
- CSV for persistent data

## How to Run
```bash
pip install flask
python app.py
```
Visit: `http://127.0.0.1:5000`

## Folder Structure
```
project/
├── app.py
├── expenses.csv
├── templates/
│   ├── index.html
│   ├── add.html
│   └── summary.html
└── static/
    └── style.css
```
