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
import sys
import importlib
import random
import re
import inspect

# these are our sub-modules
from core import SessionStorage
import modules

# -----------------------------
# MICA INTRO
# -----------------------------
def _random_font():
    fonts = ['starwars', 'isometric1', 'isometric2', 'slant']
    min_index = 0
    max_index = len(fonts)-1
    select = random.randint(min_index, max_index)
    return fonts[select]


f_large = Figlet(font=_random_font())
BASE_URL = config['SERVER_API_URL']


# the intro printer
def _show_intro():
    os.system('clear')
    print('----------------------------')
    print('Welcome to ..\n')
    print(f_large.renderText('MiCA'))
    print('MiCA = A Framework for microservice-based Simulations of Cyber Attacks\n')
    print('Developer & Creater: Andreas Zinkl')
    print('E-Mail: zinklandi@gmail.com')
    print('----------------------------')


# -----------------------------
# Initialization and Logic
# -----------------------------

CLI_MODULES = 'CLI_MODULES'
sessionStorage = SessionStorage()

def _init_modules():
    list_of_modules = dir(sys.modules['modules'])
    mods = sessionStorage.get_value(CLI_MODULES)
    if not mods:
        mods = []
    mods.extend([module for module in list_of_modules if not module.startswith('_')])
    sessionStorage.store(CLI_MODULES, mods)


# -----------------------------
# MiCA Startup
# -----------------------------

if __name__ == '__main__':
    # always show the intro on startup
    _show_intro()

    # initialize the modules
    _init_modules()

    # set the current step to startup
    current_step = 'startup'
    result = []

    # run the cli within a while loop
    try:
        while(True):

            # workaround - if it is not a array (string or none etc..)
            # then just make it an empty array
            if not type(result) is list:
                result = []

            # ask the question first
            next_step, result = questions.ask(current_step, result)

            # save the results of this step
            if result:
                sessionStorage.store(current_step, result)

            # check if we have a module to execute
            CLI_MODS = sessionStorage.get_value(CLI_MODULES)
            if next_step in CLI_MODS:
                cli_module_string = 'modules.{}'.format(next_step)
                cli_module = importlib.import_module(cli_module_string)
                cli_result = cli_module.execute(sessionStorage)

                # as failure we should get the next step
                if not cli_result:
                    next_step = 'failure'

                # normally we need to use that results, if we should select something
                # if it is just a object or boolean, we should not use it
                if isinstance(cli_result, bool):
                    result = None
                else:
                    result = cli_result
            
            # now set the current step as next step
            current_step = next_step
    except Exception as ex:
        print('Shutting down the CLI because of an error: {}'.format(ex))
        exit(0)
