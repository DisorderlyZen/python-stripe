from stripe import Stripe

class Charges(object):
    charges_action = "charges"
    refund_action = "refund"

    def __init__(self, stripe):
        self.stripe = stripe

    def charge(self, data):
        response = self.stripe.postRequest("charges", data)
        
        return response

    def getCharge(self, charge_id):
        url = self._constructChargeAction(charge_id)
        response = self.stripe.getRequest(url)
        
        return response

    def listCharges(self, data=None):
        response = self.stripe.getRequest(self.__class__.charges_action, data)
        
        return response

    def refund(self, charge_id, amount):
        url = "{}/{}".format(self._constructChargeAction(charge_id), self.refund_action)
        response = self.stripe.postRequest(url, { "amount": amount })
        
        return response

    def _constructChargeAction(self, charge_id):
        return "{}/{}".format(self.__class__.charges_action, charge_id)
    
