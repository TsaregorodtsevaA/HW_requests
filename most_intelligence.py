import requests
from pprint import pprint
url = "https://akabab.github.io/superhero-api/api/all.json"
response = requests.get(url)
all = response.json()

def the_most_intelligence(*args):
    intelligence = [] #список, в который будем добавлять все значения intelligence
    all_maximus = [] #список, в который будем добавлять супергероев с максимальными значениями intelligence
    for person in args:
        for el in all:
            if person ==el['name']:
                intelligence.append(el["powerstats"]['intelligence'])
                max_int = sorted(intelligence)
    for person in args:
        for i in all:
            if person == i['name']:
                if max_int[-1]== i["powerstats"]['intelligence']:
                    all_maximus.append(person)
    return all_maximus

print(the_most_intelligence('Captain America', 'Hulk', 'Thanos'))