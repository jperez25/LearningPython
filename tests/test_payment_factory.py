from commons.payment_factory import PaymentFactory


def test_create_payment_generates_valid_random_payment():
  payment = PaymentFactory.create_payment()

  assert 1 <= payment.amount <= 1000
  assert round(payment.amount, 2) == payment.amount
  assert payment.payment_method in {"ACH", "CARD", "VCARD", "CHECK"}
  assert payment.currency == "USD"
  assert payment.payment_id
  assert payment.payer_id
  assert payment.payee_id
  assert len({payment.payment_id, payment.payer_id, payment.payee_id}) == 3
