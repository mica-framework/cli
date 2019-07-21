import server
from core import SessionStorage

def execute(*args):
    sessionStorage = args[0]
    attack_type = sessionStorage.get_value('list_attacks')
    victims = sessionStorage.get_value('list_victims')
    
    print('### Your Configuration:')
    print('>> Attack: {}'.format(attack_type))
    print('>> Victims:')
    for victim in victims:
        print('- {}'.format(victim))
        
    return True