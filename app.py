import scrape

import datetime

import requests

from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():

    table =  scrape.main()

    date = datetime.date.today().strftime("%A %d %B")

    return render_template('page.html', name=table, date=date)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
