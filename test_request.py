import requests
import re, json
from bs4 import BeautifulSoup

mode = '1s'
user = 'luckyzakary'
url = f'https://rocketleague.tracker.network/profile/mmr/steam/{user}'
overview_page = requests.get(url)
soup = BeautifulSoup(overview_page.text, 'lxml')
player_id = re.search(r'\d+', soup.find('i', class_='ion-record').parent['href'])[0]

live_url = 'https://rocketleague.tracker.network/live/data'
data = json.dumps({'playerIds': [player_id]})
live_data = requests.post(live_url, data=data).json()
# print(live_data.json())
for stat in live_data['players'][0]['Stats']:
    if mode[0] in stat['Value']['Label']:
        mmr = stat['Value']['ValueInt']
        break
