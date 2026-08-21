#Write a program to implement a Configurable Payment Processing System Using Strategy Pattern

from abc import ABC, abstractmethod


# Abstract class
class PaymentMethod(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def pay(self):
        pass


# Concrete class
class UPI(PaymentMethod):

    def __init__(self, upi_id):
        super().__init__("UPI")
        self.upi_id = upi_id

    def pay(self):
        print("Payment done using UPI")
        print("UPI ID:", self.upi_id)


class Cash(PaymentMethod):

    def __init__(self):
        super().__init__("Cash")

    def pay(self):
        print("Payment done using Cash")


class NetBanking(PaymentMethod):

    def __init__(self, account_number):
        super().__init__("NetBanking")
        self.account_number = account_number

    def pay(self):
        print("Payment done using NetBanking")
        print("Account Number:", self.account_number)


class CreditCard(PaymentMethod):

    def __init__(self, card_number):
        super().__init__("Credit Card")
        self.card_number = card_number

    def pay(self):
        print("Payment done using Credit Card")
        print("Card Number:", self.card_number)


# Context class
class Payment:

    def __init__(self, method):
        self.method = method

    def processpayment(self):
        print("Payment Method:", self.method.name)
        self.method.pay()
        print()


# Objects
payment = Payment(UPI("user@upi"))
payment.processpayment()

payment = Payment(Cash())
payment.processpayment()

payment = Payment(NetBanking("1234567890"))
payment.processpayment()

payment = Payment(CreditCard("1234-5678-9012"))
payment.processpayment()

