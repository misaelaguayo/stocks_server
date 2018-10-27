import os

from flask import Flask, request, jsonify
import quandl

app = Flask("server")

@app.route("/<string:ticker>", methods = ["GET"])
def index(ticker):
	try: 
		quandl.ApiConfig.api_key = os.environ.get("QUANDL_KEY")
		results = quandl.get("EOD/{}".format(ticker))
	except Exception as e:
		print(e)
		return jsonify({"error": "Invalid ticker"})
	# print(results.columns)
	data = {"data": results.to_json()}
	return jsonify(data)
	
@app.route("/", methods = ["GET"])
def index2():
	return "hi"


if (__name__ == "__main__"):
	app.run(host = "0.0.0.0", port = 80, debug = True)
