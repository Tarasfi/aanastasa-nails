from flask_bootstrap import Bootstrap5
from flask import Flask, render_template, request
from db import db
from price import Price
from forms import NewNailsForm
import os 
from dotenv import load_dotenv

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


@app.route("/booking_page")
def book_nails():
    result = db.session.execute(db.select(Price))
    prices = result.scalars().all()
    return render_template("booking/booking_page.html", prices=prices)

@app.route("/add_nails", methods=['POST', 'GET'])
def add_nails():
    form = NewNailsForm()
    if request.method == "POST":
        new_nails = Price(
            title = request.form.get('title'),
            description = request.form.get('description'),
            price = request.form.get('price'),
            service_type = request.form.get('service_type')
        )
        db.session.add(new_nails)
        db.session.commit()

    return render_template("admin/add_nails.html", form=form)





if __name__ == '__main__':
    app.run(debug=True)
