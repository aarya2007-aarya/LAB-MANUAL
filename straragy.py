#Write a program to implement a Configurable Payment Processing System Using Strategy Pattern

class UPI:
    def pay(self):
        print("payment done using UPI")

class cash:
    def pay(self):
        print("payment done using cash")

class netbanking:
    def pay(self):
        print("payment done using netbanking")

class creditcard:
    def pay(self):
        print("payment done using creditcard")

class Payment:
    def __init__(self,method):
        self.method=method

    def processpayment(self):
        self.method.pay()

payment = Payment(UPI())
payment.processpayment()

payment = Payment(cash())
payment.processpayment()

payment = Payment(netbanking())
payment.processpayment()

payment = Payment(creditcard())
payment.processpayment()
