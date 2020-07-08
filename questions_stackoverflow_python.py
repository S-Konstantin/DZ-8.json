import requests

response = requests.get('https://api.stackexchange.com/2.2/questions?fromdate=1593993600&todate=1594166400&order=desc&sort=activity&tagged=Python&site=stackoverflow')

print(response.json())


