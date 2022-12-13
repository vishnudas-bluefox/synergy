# synergy
Pi hack project for future development



## BAckend 
Developed with:
* Django REST Framework 
* psql or sqlite

psql database need to manually configure in settings.py file

## API End points:
_____

### POST User registration completed
```
http://localhost:8000/register/ params?here
```
### POST Authenticate the registered user return the jwt token as cookies
```
http://localhost:8000/login/ params?here
```
### POST Update the monthly energy production capability of user in kseb db and user db for the credit system
```
http://localhost:8000/ksebsolarcapacity/ params?here
```
### POST add the points in user table when the solar pannel get updated
```
http://localhost:8000/addpoint/ params?here
```
### GET Fetch the entire user data by consumerno
```
http://localhost:8000/userdata/ params?here
```
### POST Share the point value to another user
```
http://localhost:8000/shareunit/ params?here
```
