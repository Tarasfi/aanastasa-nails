from flask import Flask, render_template
import json

app = Flask(__name__)



@app.route("/")
def home():
    with open ('data/price.json', encoding='utf-8') as p:
        prices = json.load(p)
        print(prices)
    return render_template("index.html", prices=prices)


if __name__ == '__main__':
    app.run(debug=True)
