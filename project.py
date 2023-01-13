import sys
from flask import Flask,request
app = Flask(__name__)
	
my_transaction = "nom"
@app.route('/')
def mytransaction():

	return my_transaction
	

#GET def du dictionnaire
transaction = {0:{"P1": "Romeo", "P2": "Josepha", "t": "13h30", "s": "100euros"}}
	
@app.route('/transactget', methods=['GET'])
def affiche():
	return transaction

@app.route('/transactpost' , methods = ['POST'])

def add():

	transaction[len(transaction)] = {"P1": request.form.get("P1"), "P2": request.form.get("P2")	, "t": request.form.get("t")	, "s": request.form.get("s")}
	
	return "40"
	
	
if __name__ == '__main__':
	if len(sys.argv) > 1:
		if sys.argv[1] == "check_syntax" :
			print ("Build [ok]")
			exit(0)
		else:
			print("Passed argument not supported")
			exit(1)
	app.run(debug=True)
