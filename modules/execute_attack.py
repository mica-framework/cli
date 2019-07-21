import server
from core import SessionStorage

def execute(*args):
    # get the session storage
    sessionStorage = args[0]

    # get the attack information
    attack_type = sessionStorage.get_value('list_attacks')
    victims = sessionStorage.get_value('list_victims')

    # execute the attack
    server.run_attack(attack_type, victims)

    # finalize the method by return True
    return True