import json
from policies.payment.salaried_payment import SalariedPaymentPolicy
from policies.payment.hourly_payment import HourlyPaymentPolicy
from policies.payment.freelancer_payment import FreelancerPaymentPolicy
from policies.payment.intern_payment import InternPaymentPolicy

def load_payment_policies_from_json(path="pago.json"):
    with open(path, "r") as f:
        config = json.load(f)
    return {
        "salaried": SalariedPaymentPolicy(config["salaried"]["bonus_percent"]),
        "hourly": HourlyPaymentPolicy(config["hourly"]["bonus_threshold"], config["hourly"]["bonus_amount"]),
        "freelancer": FreelancerPaymentPolicy(),
        "intern": InternPaymentPolicy()
    }
