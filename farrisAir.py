from flask import Flask

main = Flask(__name__)
main.run(host='0.0.0.0')

@main.route('/home')
def index():
    return "test"

if __name__ == "__main__":
    main.run(debug=False)