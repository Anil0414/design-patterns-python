# strategy_pattern.py

# Strategy Interface
class PaymentStrategy:
    def pay(self, amount):
        pass


# Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} using Credit Card")


class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} using PayPal")


class UpiPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} using UPI")


# Context
class PaymentContext:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def pay_amount(self, amount):
        self.strategy.pay(amount)


# Client Code
if __name__ == "__main__":
    context = PaymentContext(CreditCardPayment())
    context.pay_amount(100)

    # Change strategy dynamically
    context.set_strategy(PayPalPayment())
    context.pay_amount(200)

    context.set_strategy(UpiPayment())
    context.pay_amount(300)