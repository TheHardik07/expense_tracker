from flask import Flask, render_template, request, redirect, url_for
import csv
import datetime

app = Flask(__name__)
FILENAME = 'expenses.csv'

def load_expenses():
    expenses = []
    try:
        with open(FILENAME, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['Amount'] = float(row['Amount'])
                expenses.append(row)
    except FileNotFoundError:
        pass
    return expenses

def save_expenses(expenses):
    with open(FILENAME, mode='w', newline='') as file:
        fieldnames = ['Date', 'Category', 'Amount']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)

@app.route('/')
def index():
    expenses = load_expenses()
    return render_template('index.html', expenses=expenses)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        expenses = load_expenses()
        category = request.form['category']
        amount = float(request.form['amount'])
        date = request.form['date'] or datetime.date.today().isoformat()
        expenses.append({'Date': date, 'Category': category, 'Amount': amount})
        save_expenses(expenses)
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/summary')
def summary():
    expenses = load_expenses()
    category_totals = {}
    daily_totals = {}
    total = 0

    for exp in expenses:
        cat = exp['Category']
        date = exp['Date']
        amt = exp['Amount']
        category_totals[cat] = category_totals.get(cat, 0) + amt
        daily_totals[date] = daily_totals.get(date, 0) + amt
        total += amt

    return render_template('summary.html', category_totals=category_totals, total=total, daily_totals=daily_totals)

if __name__ == '__main__':
    app.run(debug=True)
