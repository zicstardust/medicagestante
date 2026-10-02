from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    selected_option = None
    if request.method == 'POST':
        selected_option = request.form.get('option')
        # You can process the selected option here if needed

    return render_template('index.html', option=selected_option)


if __name__ == '__main__':
    app.run(debug=True)