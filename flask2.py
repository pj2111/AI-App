# code using with request argument. 
from flask import Flask, request 
app = Flask(__name__) 

@app.route('/query_example') 
def query_example(): 
	language = request.args.get('language') 
	return '<h1> The Language is : {} </h1>'.format(language) 

if __name__ == '__main__': 
	app.run(debug=True, port=5000)
