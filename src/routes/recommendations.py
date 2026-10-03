from flask import Blueprint, render_template, request
from libs.load_recommendation import load_recommendation


recommendations_bp = Blueprint('recommendations', __name__)


@recommendations_bp.route("/condicaogestante", methods=['GET', 'POST'])
def recommendations():
    data_recommendation = None
    selected_option = None
    if request.method == 'POST':
        selected_option = request.form.get('option')
        if selected_option:
            data_recommendation = load_recommendation(selected_option)

    return render_template('recommendations/index.html',
                           option=selected_option,
                           data=data_recommendation)