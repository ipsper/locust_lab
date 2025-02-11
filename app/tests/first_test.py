import subprocess

def test_locust_run():
    result = subprocess.run(["locust", "--headless", "-u", "10", "-r", "2", "--run-time", "10s", "-H", "https://github.com/ipsper"], capture_output=True, text=True)
    assert "Requests/sec" in result.stdout, "Locust test did not run correctly"