# Run env command: source env/bin/activate
# Deactivate env command: deactivate

"""
Test server command: 
export FLASK_ENV=development
flask run
"""

"""
To connect to the database: 
sudo su root
mysql -u root -p
Password: raspberry1
"""

# Use this to create a user
# zachj MySQL Password: parris71
# Use this to create a password: https://stackoverflow.com/questions/1559955/host-xxx-xx-xxx-xxx-is-not-allowed-to-connect-to-this-mysql-server

from flask import Flask
from flask import render_template

import mysql.connector
from mysql.connector import errorcode

from authlib.integrations.flask_oauth2 import flask_oauth2

try:
    cnx = mysql.connector.connect(user='zachj', password='parris71', host='10.253.0.101', database='test_database')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnx.close()

main = Flask(__name__, template_folder="client/build", static_folder="client/build/static")

@main.route('/render-page')
def render_page(): 
    return render_template('index.html')

@main.route('/home')
def index():
    return "HOMER PAGE"

if __name__ == "__main__":
    main.run(debug=False,host='0.0.0.0')
