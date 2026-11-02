# api_app/main.py
import time
import logging
from fastapi import FastAPI, HTTPException, Request
from commons.payment import Payment

app = FastAPI()

# Temporary database simulation
fake_db = []

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("unicorn.error")


@app.middleware("http")
async def log_requests(request: Request, call_next):
  start_time = time.time()

  # Log that a request was received
  logger.info(f"➡️ INCOMING REQUEST: {request.method} {request.url.path}")

  # Process the request
  try:
    response = await call_next(request)
    process_time = (time.time() - start_time) * 1000
    logger.info(
      f"⬅️ COMPLETED: {request.method} {request.url.path} "
      f"| Status: {response.status_code} "
      f"| Took: {process_time:.2f}ms"
    )
    return response
  except Exception as e:
    logger.error(f"❌ ERROR processing {request.method} {request.url.path}: {str(e)}")
    raise e


@app.post("/payments/", response_model=Payment)
def create_payment(payment: Payment):
  logger.info(f"Processing creation of payment ID: {payment.payment_id} for amount {payment.amount}")
  fake_db.append(payment)
  return payment


@app.get("/payments/{payment_id}", response_model=Payment)
def get_payment(payment_id: str):
  logger.info(f"Looking up payment ID: {payment_id} in database...")
  for payment in fake_db:
    if payment.payment_id == payment_id:
      logger.info(f"Payment ID: {payment_id} found in database.")
      return payment
  logger.warning(f"Payment ID: {payment_id} not found in database.")
  return {"error": "Payment not found"}