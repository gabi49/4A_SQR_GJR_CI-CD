from flask import Flask, request, jsonify
import csv
import json
import sys
import hashlib
 
app = Flask(__name__)


transacTab = []
Hash_tab = []

#Importation des données depuis le fichier data.csv 
with open('data.csv') as file:
	reader = csv.reader(file)
	header = next(reader)
	for row in reader:
		sender,receiver,time,amount=row
		#print(row)
		transacTab.append({"sender":sender,
		"receiver":receiver,"time":time,
		"amount":float(amount),
		"hash":hashlib.sha256((sender+ receiver+amount+time).encode()).hexdigest()})
		Hash_tab.append(hashlib.sha256((sender+ receiver+amount+time).encode()).hexdigest())
		

@app.route('/')
def mytransaction():
	return "hello"
	
#retourne notre liste de transaction triée en fonction de la date
@app.route('/transacget', methods=['GET'])
def affiche():
	transacTab.sort(key=lambda x: x['time'])
	return jsonify(transacTab)

#Enregistre une nouvelle transaction
@app.route('/transacpost', methods=['POST'])
def add():
	data = request.get_json()
	#transac.append(data)
	transaction = {
		'time' : data['time'],
		'amount' : data['amount'],
		'sender' : data['sender'],
		'receiver' : data['receiver'],
		'hash':hashlib.sha256((data['sender'] + data['receiver'] + data['amount'] + data['time']).encode()).hexdigest()
		
	}
	transacTab.append(transaction)
	return "Transaction reussie"
	
#test avec :  
#curl --X POST -H "Content-type:application/json" --data-binary "{\"sender\":\"Josepha\", \"receiver\":\"Romeo\", \"time\":\"2021-09-10\", \"amount\":\"100\"}" http://localhost:5000/transacpost
#curl --X POST -H "Content-type:application/json" --data-binary "{\"sender\":\"Romeo\", \"receiver\":\"Gabriel\", \"time\":\"2013-03-10\", \"amount\":\"100\"}" http://localhost:5000/transacpost
#curl --X POST -H "Content-type:application/json" --data-binary "{\"sender\":\"Romeo\", \"receiver\":\"Gabriel\", \"time\":\"2013-03-10\", \"amount\":\"100\"}" http://localhost:5000/transacpost


#retourne la liste des transactions d'une personne
@app.route("/transacPerson")
def personSort ():
	personne = request.args.get("personne")
	if personne:
		personne_transaction = [p for p in transacTab if p['sender'] == personne]
		sorted_transaction = sorted(personne_transaction, key=lambda x: x['time'])
		return str(sorted_transaction)
		newTab = str(sorted_transaction)
	return "Le resultat se trouve dans le console"
#test avec curl http://localhost:5000/transacPerson?personne=Romeo

#retourne le solde d'une personne
@app.route("/balance")
def personBalance ():
	personne = request.args.get("personne")
	if personne:
		personne_transactionSend = [p for p in transacTab if p['sender'] == personne]
		balanceS = sum([t['amount'] for t in personne_transactionSend])
		personne_transactionReceive = [p for p in transacTab if p['receiver'] == personne]
		balanceR = sum([t['amount'] for t in personne_transactionReceive])
		
		if balanceS > balanceR:
			newbalance = balanceR - balanceS
			return "la solde de:" + str(personne) + "est:" + str(newbalance) + " " + "veuillez charger votre compte"
		if balanceS < balanceR:
			newbalance = balanceS - balanceR
			return "la solde de:" + str(personne) + "est:" + str(newbalance)
		return "le resultat se trouve dans la console"
#test avec curl http://localhost:5000/balance?personne=Romeo


#Vérification de l'intégrité des transactions
@app.route('/test_integ' , methods = ['GET'])
def f():
	for i in range(len(transacTab)):
		t = hashlib.sha256((transacTab[i]['receiver'] + transacTab[i]['sender'] + str(transacTab[i]['amount']) + transacTab[i]['time']).encode()).hexdigest()
		if t != Hash_tab[i]:
	  		return "True"
		       		
		else:
			return "False"
				
	return " "



	

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "check_syntax":
            print("Build [ OK ]")
            exit(0)
        else:
             print("Passed argument not supported ! Supported argument: check_syntax")
             exit(1)

    app.run(debug=True)

