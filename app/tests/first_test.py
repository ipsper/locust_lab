import subprocess

def test_locust_run():
    result = subprocess.run(["locust", "-f", "load_test.py", "--headless", "-u", "10", "-r", "2", "--run-time", "10s"], capture_output=True, text=True)
    assert "Requests/sec" in result.stdout, "Locust test did not run correctly"