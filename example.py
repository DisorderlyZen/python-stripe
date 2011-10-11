#!/usr/bin/env python

import optparse
from stripe.stripe import Stripe
from stripe.charges import Charges

def main():
    #p = optparse.OptionParser()
    #p.add_option('--person', '-p', default="world")
    #options, arguments = p.parse_args()
    charges = Charges('vtUQeOtUnYr7PGCLQ96Ul4zqpDUO4sOE')

    chargeInfo = {
        "amount": 400,
        "currency": "usd",
        "card": "tok_HxEkAd7RCjHs7m",
        "description": "Charge for site@stripe.com"
    }

    response = charges.charge(chargeInfo)
    print response

if __name__ == '__main__':
    main()

