# ================================================
# Welcome to the MiCA Framework - CLI Client
# MiCA = Microservice-based Simulation of Cyber Attacks
# --
#
# This CLI basically represents the client for the MiCA Framework.
# It provides the functionality to run attacks on the remote clients,
# install the framework or also configure the installation.
#
# For a more detailed overview of the Server please check out the README.md.
# --
#
# Developed By
# Andreas Zinkl
# E-Mail: zinklandi@gmail.com
# ================================================
# general imports
from __future__ import print_function, unicode_literals
from pyfiglet import Figlet
from config import config
import questions
import os
import random

# these are our sub-modules
import client
import installer
import manager


def _random_font():
    fonts = ['starwars', 'isometric1', 'isometric2', 'slant']
    min_index = 0
    max_index = len(fonts)-1
    select = random.randint(min_index, max_index)
    return fonts[select]


f_large = Figlet(font=_random_font())
BASE_URL = config['SERVER_API_URL']


# the intro printer
def show_intro():
    os.system('clear')
    print('----------------------------')
    print('Welcome to ..\n')
    print(f_large.renderText('MiCA'))
    print('MiCA = A Framework for microservice-based Simulations of Cyber Attacks\n')
    print('Developer & Creater: Andreas Zinkl')
    print('E-Mail: zinklandi@gmail.com')
    print('----------------------------')


# startup the cli, and look for what we'd like to do!
show_intro()    # but first show the intro :)
module, answer = questions.list('startup')  # now ask for the sub-module

# now start the sub-module part
if module == "client":
    client.show()

if module == "installer":
    installer.show()

if module == "manager":
    manager.show()
