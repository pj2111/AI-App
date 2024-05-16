from flask import Flask, request

app = Flask(__name__)

@app.route("/ap",methods=["POST"])
def dummy():
	return{"Key":"This is the post"}


@app.route("/api1",methods=["GET"])
def dummy_get():
    language = request.args.get('language') 
    return f"<html><h2>Hello {language}</h2></html>"

if __name__ == '__main__':
	app.run()