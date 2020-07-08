import requests

file_name = 'my_file.txt'

with open(file_name, encoding='utf-8') as file:
    read_file = file.read()

header = {'Authorization' : 'должен быть токен'}
file_path = requests.get('https://cloud-api.yandex.net:443/v1/disk/resources/upload?path=%2Fmy_file', headers=header)

href = file_path.json()['href']

file_add = requests.put(href, data=file_name)

print(file_add.text)