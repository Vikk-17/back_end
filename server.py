from flask import Flask, redirect, render_template, request, redirect
import csv


def write_to_csv(data):
    with open('db.csv', mode='a', newline='') as dbase:
        email = data['email']
        sub = data['subject']
        des = data['description']
        
        csv_data = csv.writer(dbase, delimiter=',', quotechar="|", quoting=csv.QUOTE_MINIMAL)
        csv_data.writerow([email, sub, des])


def write_to_txt(data):
    with open('db.txt', mode='a') as db:
        email = data['email']
        sub = data['subject']
        des = data['description']
        file = db.write(f'\n{email}, {sub} {des}')

app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(f'{page_name}')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == "POST":
        data = request.form.to_dict()
        # print(data)
        write_to_csv(data)
        return redirect ('/thanks.html')
    else:
        return "Oops! Something went wrong"