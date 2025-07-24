from flask import Flask, render_template
import json
from db import db
from price import Price



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///price.db"
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def home():

    return render_template("main/index.html")


@app.route("/book_nails")
def book_nails():
    with open ('data/price.json', encoding='utf-8') as p:
        prices = json.load(p)

    return render_template("booking/booking_page.html", prices=prices)





if __name__ == '__main__':
    app.run(debug=True)
