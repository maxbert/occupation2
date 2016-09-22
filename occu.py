from flask import Flask, render_template #get the Flask classes methods
import random

JOBS = {}
app = Flask(__name__)#constructor

def opener():
    a = open("occupations.csv", "r")
    b = a.read().split("\n")
    b = b[1:]
    for i in range(len(b) -2):
        if b[i][0] == "\"":
            JOBS[b[i].split("\"")[1]] = float(b[i].split("\"")[2][1:])
        else:    
            JOBS[b[i].split(",")[0]] = float(b[i].split(",")[1])

opener()

def chooser():
    choices = []
    jobs = JOBS.keys()
    for i in jobs:
        for j in range(int(JOBS[i] * 10) -1 ):
            choices.append(i)
    a = random.randrange(len(choices))
    return(choices[a])

joobs = JOBS.keys()
jebs = []
c = 0;
while c < len(joobs) - 1:
    jebs[c] = joobs[c] + "" + str(JOBS[joobs[c]])
    c = c + 1

@app.route("/")
def hey():
    return render_template('main.html', message = chooser(), jobs = jebs)


if __name__ == "__main__":
    app.debug = True
    app.run()#start webserver
  
