import json
import requests
from requests_jwt import JWTAuth

url = 'https://bank-api-fyle-app.herokuapp.com/api/token/'
params = {'username': 'rohit', 'password': 'rohit'}
auth = requests.post(url=url, data=params).json()

# print(auth['access'])
access = auth['access']

# url = 'https://bank-api-fyle-app.herokuapp.com/api/bank/'
params = {'ifsc': 'ABHY0065001'}
# headers = {'Authorization': access}
authe = JWTAuth(access)

# header = {'Authorization': 'Bearer ' + access}
# header = {'Authorization': 'Bearer {}'.format(access)}
# header = {'Authorization': 'token {}'.format(auth)}
# header = {'Content-Type':'application/json', 'Authorization': 'Bearer {}'.format(access)}

# print(type(auth))
# bank_details = requests.get(url=url, headers=header, params=params)


import requests
print('start')
url = "https://bank-api-fyle-app.herokuapp.com/api/bank/"

payload = ""
headers = {
    'Authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTY1NDIwNzg4LCJqdGkiOiJhYzM3N2UwZTMxYTk0ODczOTZmOTE1Y2I4NGRiNDYwNyIsInVzZXJfaWQiOjF9.ukQI82cFKSkjTjZFWEWf7EekyUQLi3arFmey9o76590",
    }
# print('almost')
response = requests.get(url=url, headers=headers, params=params)

print(response.text)



# print('Bank details: ', bank_details, bank_details)

urll = 'https://bank-api-fyle-app.herokuapp.com/api/branch/'
params = {'city': 'MUMBAI', 'bank_name': 'ABHYUDAYA COOPERATIVE BANK LIMITED'}
headers = {'Authorization': access}
# branch_details = requests.get(url=urll, params=params, auth=authe)

# print('Branch details: ', branch_details.json())
