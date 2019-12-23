try:

    import os
    import numpy as np
    from flask import Flask, render_template,request,jsonify,redirect,url_for
    from flask import redirect, url_for, request, render_template, send_file
    from io import BytesIO
    import sqlite3
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import pandas as pd
    ##from flask_api import Form
    from flask_wtf.file import FileField
    from wtforms import SubmitField
    #import flask_api
    from flask_wtf import Form
    #from flask_wtf import Form
    ##from model import multivariate_data, plot_train_history, create_time_steps, show_plot, multi_step_plot
    print('\n')
    print('Libraries Imported.')
    print('\n')

except:
    print('Some modules missing.')

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"   ##we use this whenever we use wt forms

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UploadForm()
    ##when the button is pressed, it will give us a POST method
    if request.method == "POST":
        if form.validate_on_submit():
            file_name = form.file.data
            database(name=file_name.filename, data=file_name.read())
            ##print("FILE : ".format(file_name.filename))
            return render_template("Complete.html", form=form)



    return render_template('Complete.html', form=form)

@app.route('/introduction', methods=['GET','POST'])
def introduction():

    form = UploadForm()
    if request.method == "POST":
        if form.validate_on_submit():
            file_name_1 = form.file.data

            return redirect(url_for("complete.html", form=form))

    return render_template("intro_1.html", form=form)

@app.route('/samepage', methods=['GET','POST'])
def samepage():

    form = UploadForm()
    if request.method == "POST":
        if form.validate_on_submit():
            file_name_2 = form.file.data

            return redirect(url_for("complete.html", form=form))

    return render_template("prac_1.html", form=form)

@app.route('/anotherpage', methods=['GET','POST'])
def anotherpage():

    form = UploadForm()
    if request.method == "POST":
        if form.validate_on_submit():
            file_name_3 = form.file.data

            return redirect(url_for("complete.html", form=form))

    return render_template("prac_1.html", form=form)

@app.route('/codepage', methods=['GET','POST'])
def codepage():

    form = UploadForm()
    if request.method == "POST":
        if form.validate_on_submit():
            file_name_4 = form.file.data

            return redirect(url_for("complete.html", form=form))

    return render_template("Multi_step_forecast.html", form=form)


##@app.route('/download', methods=["GET", "POST"])

class UploadForm(Form):
    file = FileField()
    submit = SubmitField("Submit")
    download = SubmitField("Download")
    introduction = SubmitField("here.")
    anotherpage = SubmitField("Another Page")
    samepage = SubmitField("Same Page")
    codepage = SubmitField("Page for Code.")

def database(name, data):
    ##giving the name of the connection
    conn = sqlite3.connect("Time_Series_Forecasting_Final.db")
    ##printting the cursor
    cursor = conn.cursor()

    cursor.execute(""" CREATE TABLE IF NOT EXISTS my_data(name TEXT, data BLOP ) """)
    cursor.execute(""" INSERT INTO my_data(name, data) VALUES (?, ?)""",(name, data))

    conn.commit()
    cursor.close()
    conn.close()

def query():
    conn = sqlite3.connect("Time_Series_Forecasting.db")
    cursor = conn.cursor()
    print("IN DATABASE FUNCTION ")
    c = cursor.execute(""" SELECT * FROM  my_data """)

    for x in c.fetchall():
        name_v = x[0]
        data_v = x[1]
        break

    conn.commit()
    cursor.close()
    conn.close()

    return send_file(BytesIO(data_v), attachment_filename='flask.csv', as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)