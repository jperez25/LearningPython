# tests/test_integration.py
from fastapi.testclient import TestClient
from app.main import app
import requests
from commons.payment import Payment
from commons.payment_factory import PaymentFactory

# FastAPI provides a built-in test client for integration testing
client = TestClient(app)

BASE_URL = "http://127.0.0.1:8000"

def test_create_and_get_payment1():
  payment = PaymentFactory.create_payment()
  response = requests.post(
      f"{BASE_URL}/payments/",
      json=payment.model_dump(),
  )
  assert response.status_code == 200


def test_create_and_get_payment():
  # 1. Prepare data using shared commons model
  new_payment = {"amount": 100.0, "currency": "USD", "payment_method": "ACH", "payment_id": "1", "payer_id": "1", "payee_id": "2"}

  # 2. Test the API POST endpoint (Integration)
  response = client.post("/payments/", json=new_payment)
  assert response.status_code == 200
  assert response.json()["amount"] == 100.0

  payment_id = response.json()["payment_id"]

  # 3. Test the API GET endpoint to verify data persistence
  get_response = client.get(f"/payments/{payment_id}")
  assert get_response.status_code == 200
  assert get_response.json()["currency"] == "USD"