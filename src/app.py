from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    selected_option = None
    if request.method == 'POST':
        selected_option = request.form.get('option')

    return render_template('index.html', option=selected_option)


#Error 404
@app.errorhandler(404)
def not_found(e):
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)