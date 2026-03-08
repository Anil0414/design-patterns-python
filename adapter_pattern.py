# adapter_pattern.py

# Existing class
class OldPaymentSystem:
    def make_payment(self, amount):
        print(f"OldPaymentSystem: Processing payment of {amount} USD")


# New class with incompatible interface
class NewPaymentSystem:
    def pay(self, amount):
        print(f"NewPaymentSystem: Paying {amount} USD")


# Adapter class
class PaymentAdapter:
    def __init__(self, new_payment_system):
        self.new_payment_system = new_payment_system

    def make_payment(self, amount):
        # Translate old interface to new interface
        self.new_payment_system.pay(amount)


# Client code
if __name__ == "__main__":
    # Old system
    old_payment = OldPaymentSystem()
    old_payment.make_payment(100)

    # Using adapter for new system
    new_payment = NewPaymentSystem()
    adapted_payment = PaymentAdapter(new_payment)
    adapted_payment.make_payment(200)