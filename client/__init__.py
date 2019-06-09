import questions
from . import attack


def show():
    # initial initialization
    attack_type = None
    victims = None
    module, answer = questions.list('client_menu', clear_console=True)
    endless_loop_counter = 10

    while True:
        if module == 'list':
            module, attack_type = attack.list_attacks()

        if module == 'victims':
            module, victims = attack.list_victims()

        if module == 'check_attack':
            module, answer = attack.check_attack(attack_type, victims)

        if module == 'run':
            module, answer = attack.run(attack_type, victims)

        if module == 'show':
            print("Error 404: This service is not available at the moment.. Work in progress..")
            pass

        if module == 'client_menu':
            module, answer = questions.list('client_menu', clear_console=True)

        if module == 'exit':
            print("Shutting down...")
            break

        endless_loop_counter -= 1
        if endless_loop_counter <= 0:
            print("Seems that we are in a endless loop..")
            module = 'exit'
