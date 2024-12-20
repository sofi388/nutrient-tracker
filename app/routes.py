from flask import render_template, request, jsonify
from .db_utils import get_calories

def index():
    return render_template('index.html')


def calculate_calorie_intake():
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    age = float(request.form['age'])
    
    if request.form.get('sex') == 'male':
        sex = 'male'
    else:
        sex = 'female'

    activity_level = request.form['activity_level']
    calorie_intake = get_calories(age, sex, activity_level)

    # calorie_intake = 10 * weight + 6.25 * height - 5 * age + 5     # BMR formula

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