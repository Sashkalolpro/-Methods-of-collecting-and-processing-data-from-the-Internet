import requests
import json

main_link = 'https://api.worldoftanks.ru/wot/'
appid = '3ef6130e9977d5e49444b0f8850a6279'
user_id = 5538376
response_gamer = requests.get(f'{main_link}account/info/?application_id={appid}&account_id={user_id}')
gamer = json.loads(response_gamer.text)

for i in gamer['data']:
  print("NickName:",gamer["data"]["5538376"]['nickname'], "\n")
  print("Проведено боев",gamer["data"]['5538376']["statistics"]["all"]["battles"],"\n")