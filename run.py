from urllib import response
import config
import requests
import pandas as pd

OAUTH_TOKEN = config.OAUTH_TOKEN
response_list = []

url = "https://api.github.com/events"

r = requests.get(url)
response_list.append(r.json())

df = pd.DataFrame.from_dict(response_list)

print(df)