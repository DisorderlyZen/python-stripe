#!/usr/bin/env python

import optparse
from stripe.stripe import Stripe
from stripe.charges import Charges

def main():
    #p = optparse.OptionParser()
    #p.add_option('--person', '-p', default="world")
    #options, arguments = p.parse_args()
    stripe = Stripe("<API_TOKEN>")
    charges = Charges(stripe)

    chargeInfo = {
        "amount": 400,
        "currency": "usd",
        "card": {
            "number": "4242424242424242",
            "exp_month": 12,
            "exp_year": 2020,
        },
        "description": "Charge for python-stripe example"
    }

    charge = charges.charge(chargeInfo)
    #chargeResponse = charges.getCharge(response["id"]);
    #response = charges.listCharges()
    response = charges.refund(charge["id"], charge["amount"])
    print response

if __name__ == '__main__':
    main()

