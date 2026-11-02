# commons/payment.py
from pydantic import BaseModel


class Payment(BaseModel):
  amount: float
  currency: str
  payment_method: str
  payment_id: str
  payer_id: str
  payee_id: str

  def process_payment(self):
    # Logic to process the payment
    pass

  def refund_payment(self, payment: Payment):
    # Logic to refund the payment
    pass