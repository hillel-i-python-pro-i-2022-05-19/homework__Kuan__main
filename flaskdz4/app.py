from faker import Faker
from flask import Flask, request
import requests
import json
import csv

app = Flask('DZ4')

fake = Faker()


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/requirements/')
def text_source():  # returning code source
    with open("app.py", 'r') as f:
        text = f.read()
    return str(text)


@app.route('/generate-users/')
def generate():     # bunch of fake emails, count is the query to get custom amount of emails
    email_list = ''
    if 'count' in request.args:
        for times in range(int(request.args['count'])):
            email_list += fake.email() + '\n'
        return email_list
    else:
        for times in range(100):
            email_list += fake.email() + '\n'
        return email_list


@app.route('/space/')
def space():        # requests method
    data = requests.get('http://api.open-notify.org/astros.json')
    json_data = json.loads(data.text)
    return str(len(json_data['people']))


@app.route('/mean/')
def count():        # may improve later with direct scanning from GDrive
    with open('people_data.csv', 'r') as file:
        csvdata = csv.DictReader(file)
        line_count = 0
        height = 0.0
        weight = 0.0
        for row in csvdata:
            height += float(row[' "Height(Inches)"'])
            weight += float(row[' "Weight(Pounds)"'])
            line_count += 1
        height = height * 2.54 / line_count
        weight = weight * 0.453592 / line_count
        return str(height) + ' ' + str(weight)


if __name__ == '__main__':
    app.run()
