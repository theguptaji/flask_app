# flask_app/flaskblog
A twitter like application with LOGIN, SCHEDULING-TIME, POST-MANAGEMENT features.

# To run 
* We are using sqlite database with this app, so we need to create a database first
* (In Mac) First install sqlite via brew.
* Create a database named "site.db":
```
sqlite3 site.db
```
* Now we need a secret key for flask security, use python console to generate one via:
```
secrets.token_hex(16)
```
* Add the configuration for sqllite database, secret key and linking gmail for forgot password feature in your bash.
  ```
  export SECRET_KEY= Secret key
  export SQLALCHEMY_DATABASE_URI='sqlite:///site.db'
  export EMAIL_USER= your_gmail_id
  export EMAIL_PASS= your_gmail_password
  ```
* Now prepare a python virtual env by:
  ```
  virtualenv venv
  source venv/bin/activate
  ```
* Install all the python libraries from __requirements.txt__ via  
  ```
  pip3 install -r requirements.txt
  ```
* from terminal  
  ```
  export FLASK_APP=flaskblog
  flask run
  ```
