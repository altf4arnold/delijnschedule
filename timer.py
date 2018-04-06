def webrequest(stop, vehicles):
	return json.load(request.urlopen("https://www.delijn.be/rise-api-core/haltes/vertrekken/{}/{}".format(stop,vehicles)))

def sort(data_out_json):
	return data_out_json["lijnen"]

def display(data,vehicles,terminal):	
	if terminal=="bash":
		os.system("clear")
	elif terminal=="dos":
		os.system("cls")
	turns=0
	while turns<vehicles:
		output=data[turns]
		print (output["lijnNummerPubliek"],"\t\t\t",output["vertrekTijd"],"\n")
		turns = turns+1

from urllib import request
import json
import os
import time


stop_nb =
vehicles_nb =
terminal_name="bash"


while True:
	display(sort(webrequest(stop_nb,vehicles_nb)),vehicles_nb,terminal_name)
	time.sleep(1)

##Made with ❤ by Altf4