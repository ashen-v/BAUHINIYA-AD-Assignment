# BAUHINIA online ordering system for ESOFT HND assignment Application development

simple web application made using mainly fastAPI framework. features includes
role based access: 
users can register,login browser products, add them to carts get total price and checkout with cash on delivery while checking address
admins can view total product quantity and amount add new products in admin dashboard


<br><br><br>

## -- Features --

1. JWT- based authetication ( 1 hours per session (60 minutes) session time can be changed by changing 
variable ACESS_TOKEN_EXPIRE_MINUTES variable  in app/oauth2.py)
2. password hashing using bycrypt
3. simple REST APIs uses POST, GET
4. Jinja2 templates for front end
5. PostgresSQL for database SQLAlchemy for ORM
6. Oauth2 Password requestform for login
<br><br><br>


## --- requirements ---

1. python 3.9 +
2. postgreSQL
<br><br><br>


## --- How to setup ---

--database--

1. Install PostgreSQL from https://www.postgresql.org/download/ and make sure the PostgreSQL
is running on the default port (5432).(open pgadmin4 right click server > properties > connection
2. create database named "BAUHINIA" in that database use username - "postgres" and password - "0000")


-other DBMS-

1. makesure SQL alchemy supports it and install supporting driver library
2. change the connection string on app/database.py to match your DBMS, server and database
<br><br><br>


## -- setting up python --

1. set up a python virtual environment (optional) - Recommended
2. run "pip install -r requirements.txt" in cmd
<br><br><br>


## -- launch the application--

1. run "uvicorn app.main:app" in cmd
2. ctrl click the http looks something like this http://127.0.0.1:8000. it will open this on web browser
3. in browser navigate to http://127.0.0.1:8000/ for home page
<br><br><br>


## --- Documentation ---

5. to acess swagger docs navigate to http://127.0.0.1:8000/docs in browser
6. to acess ReDocs navigate to  navigate to http://127.0.0.1:8000/redoc in browser

## --- get Admin Access ---
admin users can't be created using the login register front-end webpage navigate to http://127.0.0.1:8000/docs
see register schema and send a POST request accordingly change "role" : "user" to "admin" in the POST request.
or use POSTMAN and send a POST request to http://127.0.0.1:8000/register/

{ 
    "username" : "username",
    "email" : "username@gmail.com",
    "address": "address",
    "phone1" : 11111 ,
    "phone2" : 111111 ,
    "password" : "password"
    "role" : "admin"
}
