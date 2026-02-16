from flask_bootstrap import Bootstrap5
from flask import Flask, render_template, request, redirect, url_for
from db import db

from price import Price
from forms import NewNailsForm, EditPriceForm

import os 
from dotenv import load_dotenv

from admin import admin_bp

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///price.db"
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
db.init_app(app)

bootstrap = Bootstrap5(app)

with app.app_context():
    db.create_all()

@app.route("/")
def home():

    return render_template("main/index.html")


@app.route("/booking_page", methods=['POST', 'GET'])
def book_nails():
    result = db.session.execute(db.select(Price))
    prices = result.scalars().all()
    return render_template("booking/booking_page.html", prices=prices)

app.register_blueprint(admin_bp, url_prefix="/admin")



if __name__ == '__main__':
    app.run(debug=True)
