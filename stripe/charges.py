from stripe import Stripe

class Charges(Stripe):

    def __init__(self, api_key, password = ""):
        Stripe.__init__(self, api_key, password)

    def charge(self, data):
        return self._postRequest("charges", data)
    
