# beskrivning av det locust interfasce api

1. [locust](https://locust.io/)
2. [locust python api](https://docs.locust.io/en/stable/quickstart.html)

# setup env

cd repo/locust_lab/app
python3 -m venv locust_lab_venv
source locust_lab_venv/bin/activate
python3 -m pip install -r requirements.txt

## windows

Set-ExecutionPolicy Unrestricted -Scope Process
Yes to all A
python.exe -m venv locust_lab_venv
locust_lab_venv\Scripts\Activate.ps1
python3 -m pip install -r requirements.txt

# run locust as webserver

locust -f locustfile.py --host https://example.com --web-port 9000

http://localhost:9000

curl -X POST -H "Content-Type: application/json" -d '{"locust_count": 10, "spawn_rate": 2}' http://127.0.0.1:9000/swarm
curl -X POST -H "Content-Type: application/json" -d '{"user_count": 10, "spawn_rate": 2}' http://127.0.0.1:9000/swarm

curl -X POST http://localhost:9000/swarm -H "Content-Type: application/json" -d '{
"user_count": 10,
"spawn_rate": 2,
"host": "https://example.com"
}'

## linux

curl -X POST http://localhost:9000/swarm \
 -H "Content-Type: application/json" \
 -d '{
"users": 10,
"spawn_rate": 2,
"host": "http://example.com"
}'

curl -X POST http://localhost:9000/stop

curl -X GET http://localhost:9000/stats/requests

curl -X GET http://localhost:9000/stats

## windows

curl.exe -X POST http://localhost:9000/swarm -H "Content-Type: application/json" \
 -d '{
"users": 10,
"spawn_rate": 2,
"host": "http://example.com"
}'
curl.exe -X POST http://localhost:9000/swarm -H "Content-Type: application/json" -d '{"users": 10, "spawn_rate": 2, "host": "http://example.com"}'

curl.exe --% -X POST http://localhost:9000/swarm -H "Content-Type: application/json" -d "{ \"user_count\": 10, \"users\": 10, \"spawn_rate\": 2, \"host\": \"http://example.com\" }"

Invoke-RestMethod -Uri "http://localhost:9000/swarm" -Method Post -Headers @{ "Content-Type"="application/json" } -Body (@{ user_count=10; spawn_rate=2; host="http://example.com" } | ConvertTo-Json -Compress)

curl.exe -X POST http://localhost:9000/stop

curl.exe -X GET http://localhost:9000/stats/requests

curl.exe -X GET http://localhost:9000/stats

# run locust

locust --headless --users 10 --spawn-rate 1 -H https://github.com/ipsper

# run pytest

pytest -s -v -x tests/first_test.py

curl -X GET http://localhost:9000/stats/requests

## första felet

(locust_lab_venv) pnehlin@Pers-MacBook-Pro app % pytest -sx tests/first_test.py

=========================================================================================================================================================== test session starts ===========================================================================================================================================================
platform darwin -- Python 3.13.0, pytest-8.3.4, pluggy-1.5.0
rootdir: /Users/pnehlin/repo/locust_lab/app
plugins: html-4.1.1, metadata-3.1.1
collected 1 item

tests/first_test.py F

================================================================================================================================================================ FAILURES =================================================================================================================================================================
**\*\*\*\***\*\***\*\*\*\***\*\***\*\*\*\***\*\***\*\*\*\***\*\***\*\*\*\***\*\***\*\*\*\***\*\***\*\*\*\***\*\***\*\*\*\***\_**\*\*\*\***\*\***\*\*\*\***\*\***\*\*\*\***\*\***\*\*\*\***\*\***\*\*\*\***\*\***\*\*\*\***\*\***\*\*\*\***\*\***\*\*\*\*** test_locust_run **\*\*\*\***\*\***\*\*\*\***\*\***\*\*\*\***\*\***\*\*\*\***\*\***\*\*\*\***\*\***\*\*\*\***\*\***\*\*\*\***\*\***\*\*\*\***\_**\*\*\*\***\*\***\*\*\*\***\*\***\*\*\*\***\*\***\*\*\*\***\*\***\*\*\*\***\*\***\*\*\*\***\*\***\*\*\*\***\*\***\*\*\*\***

    def test_locust_run():
        result = subprocess.run(["locust", "--headless", "-u", "10", "-r", "2", "--run-time", "10s", "-H", "https://github.com/ipsper"], capture_output=True, text=True)

>       assert "Requests/sec" in result.stdout, "Locust test did not run correctly"
>
> E AssertionError: Locust test did not run correctly
> E assert 'Requests/sec' in ''
> E + where '' = CompletedProcess(args=['locust', '--headless', '-u', '10', '-r', '2', '--run-time', '10s', '-H', 'https://github.com/i... 140 170 190 210 380 500 500 500 500 500 500 42\n\n').stdout

tests/first_test.py:5: AssertionError
========================================================================================================================================================= short test summary info =========================================================================================================================================================
FAILED tests/first_test.py::test_locust_run - AssertionError: Locust test did not run correctly
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! stopping after 1 failures !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
=========================================================================================================================================================== 1 failed in 10.24s ============================================================================================================================================================
