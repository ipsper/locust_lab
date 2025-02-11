import subprocess
import re

def test_locust_run():
    result = subprocess.run(["locust", "--headless", "--users", "10", "--spawn-rate", "1", "--run-time", "10s", "-H", "https://github.com/ipsper"],
                             capture_output=True, text=True)
    print("test_locust_run", result.stdout)
    status_codes = re.findall(r'HTTP/1.1" (\d{3})', result.stdout)
    assert '200' in status_codes, f"Expected status code 200, but got {status_codes}"

    assert "Response time percentiles" in result.stdout

    assert "Requests/sec" in result.stdout