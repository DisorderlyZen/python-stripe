from stripe import Stripe

class Customers(object):
    customers_action = "customers"

    def __init__(self, stripe):
        self.stripe = stripe

    def createCustomer(self, data):
        pass

    def getCustomer(self, customerId):
        pass

    def updateCustomer(self, customerId, data):
        pass

    def listCustomers(self, data=None):
        pass
