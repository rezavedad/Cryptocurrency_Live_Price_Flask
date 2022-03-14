from flask import Flask, render_template, request, flash
import requests
import json
#import re

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

@app.route("/")
def index():
	#flash("what's your name?")
	return render_template("index.html")

@app.route("/btc", methods=['POST', 'GET'])
def btc():
	r = requests.get('https://api.coinlore.net/api/ticker/?id=90')
	btc_l = r.json()
	btc_d = btc_l[0]
	btc_price = btc_d['price_usd']
	btc_24 = btc_d['percent_change_24h']

	#flash("Hi " + str(request.form['name_input']) + ", great to see you!")
	#q=re.match(r'\'price_usd\': \'(\d.*)\', str)
	flash("Price [USD] : " + btc_price + " and  Percent change in 24h : " + btc_24 )
	return render_template("index.html")

@app.route("/eth", methods=['POST', 'GET'])
def eth():
	reth = requests.get('https://api.coinlore.net/api/ticker/?id=80')
	eth_l = reth.json()
	eth_d = eth_l[0]
	eth_price = eth_d['price_usd']
	eth_24 = eth_d['percent_change_24h']
	#flash("Hi " + str(request.form['name_input']) + ", great to see you!")
	flash("Price [USD] : " + eth_price + " and  Percent change in 24h : " + eth_24)
	return render_template("index.html")

if __name__ == "__main__":
	app.run(debug=True, host="127.0.0.1") # host="127.0.0.1" local
