from flask import Flask
# using mssql

main = Flask(__name__)

@main.route('/home')
def index():
    return "zach is a genius."

if __name__ == "__main__":
    main.run(debug=False,host='0.0.0.0')    