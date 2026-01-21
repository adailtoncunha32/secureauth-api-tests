import requests
import os
BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:9000")

def test_health():
    r = requests.get(f"{BASE_URL}/health", timeout=10)
    assert r.status_code.status_code == 200
