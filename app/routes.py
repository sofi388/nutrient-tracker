# routes.py
from flask import render_template, request, jsonify


def index():
    return render_template('index.html')


def calculate_calorie_intake():
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    age = float(request.form['age'])

    calorie_intake = 10 * weight + 6.25 * height - 5 * age + 5     # BMR formula for beginning

    return render_template('index.html', calories=calorie_intake)


def check_ferrum_level():
    age = float(request.form['age_ferrum'])
    ferrum = float(request.form['ferrum'])
    res = ""
    if ferrum > 400:
        res = "high"
    elif ferrum < 400 and ferrum > 30:
        res = "normal"
    else:
        res = "low"

    return render_template('index.html', ferrum_level = res)