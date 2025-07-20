from .base_payment import PaymentPolicy

class InternPaymentPolicy(PaymentPolicy):
    def calculate_payment(self, employee):
        employee.log_transaction("payment", 0, "Interns not paid")
        return 0
