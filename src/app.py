from flask import Flask, redirect, render_template, request, url_for
from libs.load_recommendation import load_recommendation

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    data_recommendation = None
    selected_option = None
    if request.method == 'POST':
        selected_option = request.form.get('option')
        if selected_option:
            data_recommendation = load_recommendation(selected_option)

    return render_template('index.html',
                           option=selected_option,
                           data=data_recommendation)


#Error 404
@app.errorhandler(404)
def not_found(e):
    return redirect(url_for('index'))
