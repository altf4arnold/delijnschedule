"""
This is a small program who has the purpose to print the delijn
public transportation real time schedule on a terminal.
"""

import json
import os
import time
import whatwewant
from urllib import request


def webrequest(stop, vehicles, previous = {'lijnen' : [], 'huidigeTijd': '00:00', 'huidigeDag': 'maandag'}):
	"""
	This function has to make the API request. If it can't, it will return the
	previous API result if provided. otherwise, it will return just enough
	to not crash the entire program.
	"""
	try:
		toreturn = json.load(request.urlopen("https://www.delijn.be/rise-api-core/haltes/vertrekken/{}/{}".format(stop,vehicles)))
	except:
		toreturn = previous
	return toreturn


def organising(data):
	"""
	This function has been made to only keep the data that we are interested in
	it returns a dictionnary that contains the entire stack of information
	that we will display.
	"""
	time = data['huidigeDag'] + data['huidigeTijd']
	busses = data['lijnen']
	return {'time': time, 'lines': busses}
	
