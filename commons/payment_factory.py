import random
from uuid import uuid4

from commons.payment import Payment


class PaymentFactory:
  PAYMENT_METHODS = ("ACH", "CARD", "VCARD", "CHECK")

  @classmethod
  def create_payment(cls) -> Payment:
    amount = random.randint(100, 100_000) / 100
    return Payment(
      amount=amount,
      currency="USD",
      payment_method=random.choice(cls.PAYMENT_METHODS),
      payment_id=str(uuid4()),
      payer_id=str(uuid4()),
      payee_id=str(uuid4()),
    )
