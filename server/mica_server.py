import requests
from config import config

BASE_URL = config['SERVER_API_URL']


def list_attacks():
    print(">> loading attacks...")
    response = requests.get(BASE_URL + "/list")
    attacks = response.json()
    if attacks['data']:
        return attacks['data']
    else:
        return []


def list_victims():
    # request the victims
    print(">> loading victims...")
    response = requests.get(BASE_URL + "/victims")
    json_response = response.json()

    # get the data from the response
    data = json_response['data']
    if not data or len(data) <= 0:
        return []

    # now get the victims data
    victims = data['victims']
    if victims:
        return victims
    else:
        return []


def run_attack(attack_name, victim_list):

    data = {
        'attack': attack_name,
        'victims': victim_list
    }
    print(data)

    response = requests.post(BASE_URL + "/attack", json=data)
    if response.status_code != 200:
        print(response.text)
