from .base_payment import PaymentPolicy

class FreelancerPaymentPolicy(PaymentPolicy):
    def calculate_payment(self, employee):
        total = sum(p["amount"] for p in employee.projects)
        employee.log_transaction("payment", total, "Freelancer project payout")
        return total
