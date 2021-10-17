import requests
import datetime as dt
import os
from dotenv import load_dotenv
load_dotenv()

pixela_endpoint = 'https://pixe.la/v1/users'
username = os.getenv('USERNAME')
token = os.getenv('TOKEN')

user_params = {
    'token': token,
    'username': username,
    'agreeTermsOfService':'yes',
    'notMinor':'yes',
}
# response = requests.post(url=pixela_endpoint, json=user_params)
graph_endpoint = 'https://pixe.la/v1/users/{}/graphs'.format(username)

graph_config = {
    'id': 'graph1',
    'name':'100-days-of-code',
    'unit':'minutes',
    'type':'int',
    'color':'sora'
}

headers = {
    'X-USER-TOKEN': token,
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

# $ curl -X POST https://pixe.la/v1/users/a-know/graphs/test-graph -H 'X-USER-TOKEN:thisissecret' -d '{"date":"20180915","quantity":"5"}'
# {"message":"Success.","isSuccess":true}
pixel_endpoint = 'https://pixe.la/v1/users/{}/graphs/{}'.format(username, graph_config['id'])

pixel_config = {
    'date': dt.datetime.now().strftime('%Y%m%d'),
    'quantity': '120',
}

# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)

# print(response.text)