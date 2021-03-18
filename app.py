# Run env command: source env/bin/activate
# Deactivate env command: deactivate
"""
Test server command: 
export FLASK_ENV=development
flask run
"""

from flask import Flask
from flask import render_template

main = Flask(__name__, template_folder="client/build", static_folder="client/build/static")

@main.route('/render-page')
def render_page(): 
    return render_template('index.html')

@main.route('/home')
def index():
    return "HOMER PAGE"

if __name__ == "__main__":
    main.run(debug=False,host='0.0.0.0')