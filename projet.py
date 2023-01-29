from flask import Flask, request, jsonify
import json
 
app = Flask(__name__)


transacTab = []
@app.route('/')
def mytransaction():
	return "hello"
	
#retourne notre liste de transaction triée en fonction de la date
@app.route('/transacget', methods=['GET'])
def affiche():
	transacTab.sort(key=lambda x: x['time'])
	return transacTab

#Enregistre une nouvelle transaction
@app.route('/transacpost', methods=['POST'])
def add():
	data = request.get_json()
	#transac.append(data)
	transaction = {
		'time' : data['time'],
		'amount' : data['amount'],
		'sender' : data['sender'],
		'reveiver' : data['receiver']
	}
	transacTab.append(transaction)
	return "Transaction reussie"
	
#test avec curl --X POST -H "Content-type:application/json" --data-binary "{\"sender\":\"Josepha\", \"receiver\":\"Romeo\", \"time\":\"2021-09-10\", \"amount\":\"100\"}" http://localhost:5000/transacpost

#curl --X POST -H "Content-type:application/json" --data-binary "{\"sender\":\"Romeo\", \"receiver\":\"Gabriel\", \"time\":\"2013-03-10\", \"amount\":\"100\"}" http://localhost:5000/transacpost

#curl --X POST -H "Content-type:application/json" --data-binary "{\"sender\":\"Romeo\", \"receiver\":\"Gabriel\", \"time\":\"2013-03-10\", \"amount\":\"100\"}" http://localhost:5000/transacpost


@app.route("/transacPerson")
def personSort ():
	personne = request.args.get("personne")
	if personne:
		personne_transaction = [p for p in transacTab if p['sender'] == personne]
		sorted_transaction = sorted(personne_transaction, key=lambda x: x['time'])
		return str(sorted_transaction)
		newTab = str(sorted_transaction)
	return "Le resultat se trouve dans le console"


@app.route("/balance")
def personBalance ():
	personne = request.args.get("personne")
	if personne:
		personne_transactionSend = [p for p in transacTab if p['sender'] == personne]
		balanceS = sum([t['amount'] for t in personne_transactionSend])
		personne_transactionReceive = [p for p in transacTab if p['receiver'] == personne]
		balanceR = sum([t['amount'] for t in personne_transactionReceive])
		if balanceS > balanceR:
			return "la solde de {personne} est {balanceR - balanceS}"
		if balanceS < balanceR:
			return "la solde de {personne} est {balanceS - balanceR}"
		return "le resultat se trouve dans la console"




	

if __name__ == '__main__':
	app.run(debug=true)

