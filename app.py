from flask import Flask,render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("test.html")


app.run(debug=True,host='0.0.0.0',port=3000)