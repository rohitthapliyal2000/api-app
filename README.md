The Backend application is Hosted on Heroku.

Here is the link to the api root: [http://bank-api-fyle-app.herokuapp.com/](http://bank-api-fyle-app.herokuapp.com/)


## List of APIs:


### Generating JWT token:

POST request at [http://bank-api-fyle-app.herokuapp.com/api/token/](http://bank-api-fyle-app.herokuapp.com/api/token/)

Params: username, password

Auth: None

Return value: access token, refresh token


### Refreshing JWT token:

POST request at [http://bank-api-fyle-app.herokuapp.com/api/token/refresh](http://bank-api-fyle-app.herokuapp.com/api/token/refresh)

Params: jwt access token

Auth: None

Return value: access token


### Feeding data from csv:

GET request at [http://bank-api-fyle-app.herokuapp.com/api/feed/](http://bank-api-fyle-app.herokuapp.com/api/feed/)

Auth: None


### Getting bank data from ifsc:

GET request at [http://bank-api-fyle-app.herokuapp.com/api/bank/](http://bank-api-fyle-app.herokuapp.com/api/bank/)

Params: ifsc

Auth: access token

Return value: Serialized json for bank model


### Getting branch data from city and bank_name:

GET request at [http://bank-api-fyle-app.herokuapp.com/api/branch/](http://bank-api-fyle-app.herokuapp.com/api/branch/)

Params: city, bank_name

Auth: access token

Return value: Array of serialized json for bank models
