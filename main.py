from flask import Flask, render_template

web = Flask(__name__)


@web.route("/")
def home():
	return render_template("home.html")

@web.route("/api/v1/<station>/<date>")
def about(station, date):
	temperature = 23
	return {"station": station,
			"date": date,
			"temperature": temperature}

if __name__ = "__main__":
	web.run(debug=True)
