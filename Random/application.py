from flask import Flask, render_template #render_template is for linking with html strings
import datetime
app = Flask(__name__)

@app.route("/")
def index():
    var = datetime.datetime.now()
    if var.month == 1 and var.day == 1:
        empregada = True
    return render_template('index.html', var=var) #only looks inside a templates page