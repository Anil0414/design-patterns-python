# factory_pattern.py

class CreditCard:
    def pay(self):
        print("Processing Credit Card Payment")


class PayPal:
    def pay(self):
        print("Processing PayPal Payment")


class UPI:
    def pay(self):
        print("Processing UPI Payment")


class PaymentFactory:

    @staticmethod
    def create_payment(method):

        if method == "credit":
            return CreditCard()

        elif method == "paypal":
            return PayPal()

        elif method == "upi":
            return UPI()

        else:
            raise ValueError("Unknown Payment Method")


# Client Code
if __name__ == "__main__":

    payment = PaymentFactory.create_payment("credit")
    payment.pay()