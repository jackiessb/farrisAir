# Farris Air
### _Air Drop for Honors_

## Development
To activate the virtual environment: 
```sh
source env/bin/activate
```

Deactivate the virtual environment: 
```sh
deactivate
```

To run server development environment:
```sh
export FLASK_ENV=development
flask run
```

If you add any new modules, run this command to update server requirements
```sh
pip freeze > requirements.txt
```

To check for requirements
```sh
py -m pip install -r requirements.txt
```