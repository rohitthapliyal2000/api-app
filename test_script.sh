curl -X POST \
  https://bank-api-fyle-app.herokuapp.com/api/token/ \
  -H 'Accept: */*' \
  -H 'Accept-Encoding: gzip, deflate' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Content-Length: 46' \
  -H 'Content-Type: application/json' \
  -H 'Cookie: csrftoken=baf7Gr0KhZ3fworUJn5nIpKYeIa6AIUkhLLZE0Gs70ME4OeQygdJXBWjghzVNBEt' \
  -H 'Host: bank-api-fyle-app.herokuapp.com' \
  -H 'Postman-Token: 64230e41-1b62-489f-9f0d-12227281846a,f25d20e0-703c-460c-a5c1-3b5b6b6e8219' \
  -H 'User-Agent: PostmanRuntime/7.16.3' \
  -H 'cache-control: no-cache' \
  -d '{
	"username": "rohit",
	"password": "rohit"
}'

echo "\n\n\n\n"

curl -X GET \
  https://bank-api-fyle-app.herokuapp.com/api/bank/ABHY0065001/ \
  -H 'Accept: */*' \
  -H 'Accept-Encoding: gzip, deflate' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTY3MDYzNDY5LCJqdGkiOiI2YmVkNWVmMDM3Yjg0MmVhYjQwODMyOTAwYWI2OGI0YyIsInVzZXJfaWQiOjF9.okMQgl5p0HP0uJFfTtL-IctC2-NjQ0fQI0zCp4HzUfc' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Cookie: csrftoken=baf7Gr0KhZ3fworUJn5nIpKYeIa6AIUkhLLZE0Gs70ME4OeQygdJXBWjghzVNBEt' \
  -H 'Host: bank-api-fyle-app.herokuapp.com' \
  -H 'Postman-Token: 40a6f8af-9cff-41d8-8da6-19b3703a8f09,575c33da-d2fb-4a61-b030-0a602aacc496' \
  -H 'User-Agent: PostmanRuntime/7.16.3' \
  -H 'cache-control: no-cache'

echo "\n\n\n\n"

curl -X GET \
  'https://bank-api-fyle-app.herokuapp.com/api/branch/ABHYUDAYA%20COOPERATIVE%20BANK%20LIMITED/MUMBAI/?limit=3' \
  -H 'Accept: */*' \
  -H 'Accept-Encoding: gzip, deflate' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTY3MDYzNDY5LCJqdGkiOiI2YmVkNWVmMDM3Yjg0MmVhYjQwODMyOTAwYWI2OGI0YyIsInVzZXJfaWQiOjF9.okMQgl5p0HP0uJFfTtL-IctC2-NjQ0fQI0zCp4HzUfc' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Cookie: csrftoken=baf7Gr0KhZ3fworUJn5nIpKYeIa6AIUkhLLZE0Gs70ME4OeQygdJXBWjghzVNBEt' \
  -H 'Host: bank-api-fyle-app.herokuapp.com' \
  -H 'Postman-Token: adf5ef5f-019d-4c3a-b428-792d406f1f4f,c1487dac-be7e-4d47-83f0-68c49d01bede' \
  -H 'User-Agent: PostmanRuntime/7.16.3' \
  -H 'cache-control: no-cache'