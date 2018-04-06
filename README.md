# What it does :

This program is a very simple python3 program that output the realtime schedule on a DeLijn bus stop

# Dependecies : 

* urllib
* json
* time
* python 3.6 or above

# Setup:

Modify the vars in the timer.py

* stop_nb has to be the ID of the stop (you can find it on google maps)
* vehicles_nb has to be the number of vehicles you want to get the information from
* terminal_name : depends of the operating system you are using

# Terminals :

Currently, we have support for windows and linux.

if you are on linux, then your terminal is : bash
if you are on windows, (go to linux) then your terminal is : dos

Warning : you have to put the terminal name betwen "". For example : "bash" or "dos"

# How to run :

if you are on arch (are you really reading this doc?!?) ```python timer.py```

if you are on another linux distro wich has his default python in 2.X, ```python3 timer.py```

if you are on windows (serioussly, go to linux) it depends of how your machine is going to be configured... it will be a surprise

# Bugs to fix : 

When there are no vehicles anymore or that we take to much vehicles, we get errors