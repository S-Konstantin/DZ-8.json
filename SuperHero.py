import requests

def intelligence_hulk():
    response = requests.get('https://www.superheroapi.com/api.php/2619421814940190/search/Hulk')
    intelligence_hulk = response.json()['results'][0]['powerstats']['intelligence']

    return f'Hulk {intelligence_hulk}'


def intelligence_captain_america():
    response = requests.get('https://www.superheroapi.com/api.php/2619421814940190/search/Captain America')
    intelligence_captain_america = response.json()['results'][0]['powerstats']['intelligence']

    return f'captain_america {intelligence_captain_america}'


def intelligence_thanos():
    response = requests.get('https://www.superheroapi.com/api.php/2619421814940190/search/Thanos')
    intelligence_thanos = response.json()['results'][0]['powerstats']['intelligence']

    return f'thanos {intelligence_thanos}'


def win_intelligence_hero():
    intelligence_total = [intelligence_hulk()] + [intelligence_thanos()] + [intelligence_captain_america()]

    print(f'Самый большой intelligence у Super Hero: {max(intelligence_total)}')

win_intelligence_hero()