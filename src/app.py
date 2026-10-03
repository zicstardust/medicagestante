from flask import Flask, redirect, url_for
from routes.homepage import homepage_bp
from routes.recommendations import recommendations_bp
from routes.calculator import calculator_bp

app = Flask(__name__)
app.register_blueprint(homepage_bp)
app.register_blueprint(recommendations_bp)
app.register_blueprint(calculator_bp)


#Error 404
@app.errorhandler(404)
def not_found(e):
    return redirect(url_for('homepage.homepage'))