"""
This is a small program who has the purpose to print the delijn
public transportation real time schedule on a terminal.
"""

import json
import os
import time
import whatwewant
from urllib import request


def webrequest(stop, previous = {'lijnen' : [], 'huidigeTijd': '00:00', 'huidigeDag': 'maandag'}):
	"""
	This function has to make the API request. If it can't, it will return the
	previous API result if provided. otherwise, it will return just enough
	to not crash the entire program.
	"""
	try:
		toreturn = json.load(request.urlopen\
	 	("https://www.delijn.be/rise-api-core/haltes/vertrekken/{}/5"\
		.format(stop)))
	except:
		toreturn = previous
	return toreturn


def organising(data):
	"""
	This function has been made to only keep the data that we are interested in
	it returns a dictionnary that contains the entire stack of information
	that we will display.
	"""
	time = data['huidigeDag'] + "\t" + data['huidigeTijd']
	busses = data['lijnen']
	return {'time': time, 'lines': busses}


def printer(thetruth):
	"""
	This function is the one who print all the info that it got to the screen
	depending on the terminal you are using (bash or dos) it will auto-adapt
	"""
	if os.name == "nt":
		os.system("cls")
	elif os.name == "posix":
		os.system("clear")
	print(thetruth['time'] + "\n")
	for i in range(len(thetruth['lines'])):
		toprint = thetruth['lines'][i]
		print(toprint['lijnNummerPubliek'], "\t", toprint['bestemming'],\
		"\t\t\t\t", toprint['vertrekTijd'])


def main():
	"""
	Main module of all things
	"""
	brut_result = webrequest(whatwewant.stop_nb)
	data = organising(brut_result)
	while True:
		printer(data)
		time.sleep(1)
		brut_result = webrequest(whatwewant.stop_nb, brut_result)
		# brut result is provided as a failsafe if the request fails
		data = organising(brut_result)


if __name__ == '__main__':
	main()
