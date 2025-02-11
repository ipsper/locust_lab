# beskrivning av det locust interfasce api

1. [locust](https://locust.io/)
2. [locust python api](https://docs.locust.io/en/stable/quickstart.html)

# setup env

cd repo/locust_lab/app
python3 -m venv locust_lab_venv
source locust_lab_venv/bin/activate
python3 -m pip install -r requirements.txt

# run locust

locust --headless --users 10 --spawn-rate 1 -H https://github.com/ipsper

# run pytest

pytest -sx tests/first_test.py
