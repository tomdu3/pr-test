import requests
import json
from pprint import pprint

import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')


url = "https://imdb146.p.rapidapi.com/v1/find/"

querystring = {"query": "Die Hard"}

headers = {
	"X-RapidAPI-Key": API_KEY,
	"X-RapidAPI-Host": "imdb146.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

# save response to a local json file
with open('imdb.json', 'w') as f:
    json.dump(response.json(), f)

titles = [title for title in response.json()['titleResults']['results']]

titles_sorted = [title['titleNameText'] for title in sorted(titles, key=lambda x: x.get('titleReleaseText', 0))]  # nice example of use of lambda


pprint(titles_sorted)