# Transaction History Storage and Validation API

    This API aims to validate transactions arranged in a .json file
     which is directed to the validation program through stdin.
     This program validates each transaction of the json file to the API in order to
     validate and store valid transactions.

## How to run

    Download the system from the git repository and compile the docker or install on the machine
     containing python installed using the commands below.

### Install:
You must choose from type of instalation as:
#### Production
    Python Version: 3.7.9
    python3 -v venv venv
    pip install -r requirements.txt
    gunicorn --bind 0.0.0.0:56733 --worker-class eventlet -w 1 app:app

#### Development
    Python Version: 3.7.9
    python3 -v venv venv
    pip install -r ./development.txt
    ./app.py

#### Docker
    1. Compile and Run Docker
    ./create_docker.sh

### Run Validator

    ./validator < file.json
