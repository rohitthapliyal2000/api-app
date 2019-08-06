import json
import requests
from requests_jwt import JWTAuth

url = 'https://bank-api-fyle-app.herokuapp.com/api/token/'
params = {'username': 'rohit', 'password': 'rohit'}
auth = requests.post(url=url, data=params).json()

# print(auth['access'])
access = auth['access']

url = 'https://bank-api-fyle-app.herokuapp.com/api/bank/'
params = {'ifsc': 'ABHY0065001'}
header = {'Authorization': access}
authe = JWTAuth(access)

# header = {'Authorization': 'Bearer ' + access}
# header = {'Authorization': 'Bearer {}'.format(access)}
# header = {'Authorization': 'token {}'.format(auth)}
header = {'Content-Type':'application/json', 'Authorization': 'Bearer {}'.format(access)}
print(header)

# print(type(auth))
# bank_details = requests.get(url=url, auth=authe, params=params)
# print(bank_details)


import requests
print('start')
url = "https://bank-api-fyle-app.herokuapp.com/api/bank/"

# print('almost')
# response = requests.get(url=url, headers=headers, params=params)

# print(response.text)



# print('Bank details: ', bank_details, bank_details)

urll = 'https://bank-api-fyle-app.herokuapp.com/api/branch/'
params = {'city': 'MUMBAI', 'bank_name': 'ABHYUDAYA COOPERATIVE BANK LIMITED'}
# headers = {'Authorization': access}
branch_details = requests.get(url=urll, params=params, headers=header)

print('Branch details: ', branch_details)
