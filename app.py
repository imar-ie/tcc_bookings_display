from flask import Flask, render_template

from datetime import datetime

from scrape import scrape

app = Flask(__name__)

@app.route('/')
def index():

    table =  scrape()

    date = datetime.now().strftime("%A %d %B")
    
    update_time = datetime.now().strftime("%H:%M")
    
    return render_template('page.html', table=table, date=date, update_time=update_time)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
