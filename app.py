from flask import Flask, render_template, flash, request
from pymongo import MongoClient
import os

app = Flask(__name__)

app.secret_key = 'some_secret'

# change cesar:cesar to chan:chan @chan
client = MongoClient('mongodb://cesar:cesar@ds155097.mlab.com:55097/housing')
db = client.housing

main_list = []


@app.route('/', methods=["GET", "POST"])
def home():
    # db.names.insert({'name': 'chan'})
    if request.method == 'POST':
        # get parameters from post
        name = request.form["name"]
        choice1 = request.form["choice1"]
        choice2 = request.form["choice2"]
        choice3 = request.form["choice3"]
        db.names.insert({'name': name, 'list': [{'choice1': choice1, 'choice2': choice2, 'choice3': choice3}]})
        flash('Thank you for submitting :D', 'success')
        return render_template('index.html')
    else:
        print('stuff')
        cur = db.names.find({})
        names = [doc for doc in cur]
        lst = list(map(print, names))
        x = map(lambda x: print(x['name']), lst)
        return render_template('index.html')


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    collection = list(db.names.find())
    people = []
    for item in collection:
        lst = {}
        lst['name'] = item['name']
        lst['lst'] = item['list']
        people.append(lst)

    main_list = people
    return render_template('admin.html', people=people)


@app.route('/sort', methods=['GET', 'POST'])
def sort():




if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    app.debug = True
