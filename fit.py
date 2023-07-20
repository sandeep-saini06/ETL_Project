from urllib import response
import config
import requests
import pandas as pd

OAUTH_TOKEN = config.OAUTH_TOKEN
response_list = []

url = "https://www.googleapis.com/fitness/v1/users/me/dataSources"

headers = { 'content-type': 'application/json',
            'Authorization': 'Bearer %s' % OAUTH_TOKEN }
r = requests.get(url, headers=headers)
print(r.json())
#response_list.append(r.json())

#df = pd.DataFrame.from_dict(response_list)

#print(df)