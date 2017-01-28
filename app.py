from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# change cesar:cesar to chan:chan @chan
client = MongoClient('mongodb://cesar:cesar@ds155097.mlab.com:55097/housing')
db = client.housing


@app.route('/')
def home():
    # db.names.insert({'name': 'cesar'})
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0")
