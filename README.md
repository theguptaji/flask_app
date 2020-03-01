# flask_app
A twitter like application with LOGIN, SCHEDULING TIME, POST MANAGEMENT features.

* Clone the repo
* Add the configuration for sqllite database and linking gmail for forgot password feature.
  ```
  export SECRET_KEY= Secret key
  export SQLALCHEMY_DATABASE_URI='sqlite:///site.db'
  export EMAIL_USER= your_gmail_id
  export EMAIL_PASS= your_gmail_password
  ```
* To run the application, install all the python libraries from __requirements.txt__ via  
  ```
  pip3 install -r requirements.txt
  ```
* from terminal  
  ```
  export FLASK_APP=flaskblog
  flask run
  ```
