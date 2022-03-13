from flask import Flask, render_template, request, flash
import requests

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"





@app.route("/")
def index():
	#flash("what's your name?")
	return render_template("index.html")

@app.route("/btc", methods=['POST', 'GET'])
def btc():
	r = requests.get('https://api.coinlore.net/api/ticker/?id=90')
	btc = r.json()
	#flash("Hi " + str(request.form['name_input']) + ", great to see you!")
	flash(btc)
	return render_template("index.html")

@app.route("/eth", methods=['POST', 'GET'])
def eth():
	reth = requests.get('https://api.coinlore.net/api/ticker/?id=80')
	eth = reth.json()
	#flash("Hi " + str(request.form['name_input']) + ", great to see you!")
	flash(eth)
	return render_template("index.html")

if __name__ == "__main__":
	app.run(debug=True, host="127.0.0.1") # host="127.0.0.1" local
