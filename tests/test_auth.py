import os
import pytest
import requests

# Se estiver rodando no GitHub Actions, pula os testes
if os.getenv("CI") == "true":
    pytest.skip("Sem API rodando no CI", allow_module_level=True)

BASE_URL = "http://127.0.0.1:9000"

def test_health():
    response = requests.get(f"{BASE_URL}/health")
    assert response.status_code == 200
