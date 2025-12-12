from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    def __init__(self, method="Generic Payment Method"):
        self.method = method
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentMethod):
    def __init__(self, card_number, card_holder, method = "Credit Card"):
        super().__init__(method)
        self.card_number = card_number
        self.card_holder = card_holder

    def pay(self, amount):
        return f"Paid {amount}$ via {self.method}"
    
class PayPalPayment(PaymentMethod):
    def __init__(self, email, method = "PayPal"):
        super().__init__(method)
        self.email = email

    def pay(self, amount):
        return f"Paid {amount}$ via {self.method}"

payments = [CreditCardPayment("1234-5678-9012-3456", "John Doe"), PayPalPayment("john.doe@example.com")]
for p in payments:
    print(p.pay(100))