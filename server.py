import pandas as pd
from flask import Flask, request, jsonify, send_file, render_template
from main import read_file, create_reports
import shutil
import os
from flaskwebgui import FlaskUI


print(os.getcwd())
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/create_reports", methods=["POST"])
def create_reports_api():
    file = request.files["file"]
    section = request.form["section"]
    year = request.form["year"]
    sem = request.form["sem"]
    print(file, section, year, sem)
    df, subcodes, subjects = read_file(file)
    create_reports(df, section, year, sem, subcodes, subjects)

    shutil.make_archive("reports", "zip", "pdfs")
    # remove created pdfs
    os.system("rmdir /s /q pdfs")
    os.mkdir("pdfs")

    return send_file("reports.zip", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
    # FlaskUI(app=app, server="flask", fullscreen=False).run()
