import server
import questions


def list_attacks():
    # get the list form the backend
    attack_list = server.list_attacks()

    # now create the actual attack list
    if not attack_list:
        return questions.list('client_attack_list_empty')
    else:
        return questions.list('client_attack_list', attack_list)


def list_victims():
    victim_list = server.list_victims()
    if not victim_list:
        return questions.list('client_victim_list_empty')
    else:
        return questions.select('client_victim_list', victim_list)


def check_attack(attack_type, victims):
    # if there's a None value, then we got a problem! so exit the application for now
    if attack_type is None or victims is None:
        return 'exit'

    print('You selected the Attack: {}'.format(attack_type))
    print('You selected the victims:')
    for victim in victims:
        print('- {}'.format(victim))
    return questions.list('client_check_attack')


def run(attack_type, victims):
    print("Sent execution command to the Server!")
    server.run_attack(attack_type, victims)
    return questions.list('client_sent_attack')
