echo "\n\n"

curl -X POST \
  https://bank-api-fyle-app.herokuapp.com/api/token/ \
  -H 'Content-Type: application/json' \
  -H 'Host: bank-api-fyle-app.herokuapp.com' \
  -H 'Postman-Token: 1eb98ecd-3bf7-4914-91c3-60a82ab9a60f,0a728932-1b06-4fed-bfa4-5eeeb97fd2a8' \
  -H 'User-Agent: PostmanRuntime/7.15.2' \
  -H 'cache-control: no-cache' \
  -d '{
  "username": "rohit",
  "password": "rohit"
}'

echo "\n\n\n\n"

curl -X GET \
  https://bank-api-fyle-app.herokuapp.com/api/bank/ \
  -H 'Accept: */*' \
  -H 'Accept-Encoding: gzip, deflate' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTY1NTIwMTUwLCJqdGkiOiI2NjIwNmE0ZmIwYTU0ZTFjYWVlYmRiMzQ4OTFkMGExNCIsInVzZXJfaWQiOjF9.wrMndHWCpGADOIbtm6nfT2IarWTk13Wn6PEsEG8Zd20' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Content-Length: 29' \
  -H 'Content-Type: text/plain' \
  -H 'Host: bank-api-fyle-app.herokuapp.com' \
  -H 'Postman-Token: 7818ffba-46a1-4bdb-8e8d-0822a6f15125,0d7500f5-910c-4470-97d2-65b1e0c6fe0e' \
  -H 'User-Agent: PostmanRuntime/7.15.2' \
  -H 'cache-control: no-cache' \
  -d '{
    "ifsc": "ABHY0065001"
}'

echo "\n\n\n\n"

curl -X GET \
  https://bank-api-fyle-app.herokuapp.com/api/branch/ \
  -H 'Accept: */*' \
  -H 'Accept-Encoding: gzip, deflate' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTY1NTIwMTUwLCJqdGkiOiI2NjIwNmE0ZmIwYTU0ZTFjYWVlYmRiMzQ4OTFkMGExNCIsInVzZXJfaWQiOjF9.wrMndHWCpGADOIbtm6nfT2IarWTk13Wn6PEsEG8Zd20' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Content-Length: 79' \
  -H 'Content-Type: application/json' \
  -H 'Host: bank-api-fyle-app.herokuapp.com' \
  -H 'Postman-Token: 478102e6-ddde-455f-a1ea-f579df9283bd,a2352c88-4772-4575-80e0-9ab6fbd9647b' \
  -H 'User-Agent: PostmanRuntime/7.15.2' \
  -H 'cache-control: no-cache' \
  -d '{
    "city": "MUMBAI",
    "bank_name": "ABHYUDAYA COOPERATIVE BANK LIMITED"
}'