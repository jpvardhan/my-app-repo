import requests
BASE_URL = "http://localhost:5000"

def test_home():
    r = requests.get(f"{BASE_URL}/")
    assert r.status_code == 200
    assert "message" in r.json()

def test_health():
    r = requests.get(f"{BASE_URL}/health")
    assert r.status_code == 200
    assert r.json()["status"] == "healthy"

def test_echo():
    msg = "hello"
    r = requests.get(f"{BASE_URL}/echo/{msg}")
    assert r.status_code == 200
    assert r.json()["echo"] == msg
