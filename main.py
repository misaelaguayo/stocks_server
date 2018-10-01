import os

from flask import Flask, request, jsonify
import quandl

app = Flask("server")

@app.route("/<string:ticker>", methods = ["GET"])
def index(ticker):
	try:
		quandl.ApiConfig.api_key = os.environ.get("QUANDL_KEY")
		results = quandl.get("EOD/{ticker}".format(ticker))
	except:
		return jsonify({"error": "Invalid ticker"})
	# print(results.columns)
	data = {"data": results.to_json()}
	return jsonify(data)
	

if (__name__ == "__main__"):
	app.run(host = "0.0.0.0", port = 80, debug = True)
