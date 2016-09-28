
from flask import Flask, render_template #get the Flask classes methods
from utils import occu

app = Flask(__name__)#constructor

occu.opener()
@app.route("/occupations/")
def hey():
    return render_template('main.html', message = occu.chooser(), jobs = occu.JOBS)
@app.route("/")
def no():
    return render_template('hey.html')

@app.route("/occupation")
def yay():
    return render_template('main.html', message = occu.chooser(), jobs = occu.JOBS)
if __name__ == "__main__":
    app.debug = True
    app.run()#start webserver
