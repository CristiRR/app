from .base_payment import PaymentPolicy

class HourlyPaymentPolicy(PaymentPolicy):
    def __init__(self, bonus_threshold=160, bonus_amount=100):
        self.bonus_threshold = bonus_threshold
        self.bonus_amount = bonus_amount

    def calculate_payment(self, employee):
        base = employee.rate * employee.hours
        bonus = self.bonus_amount if employee.hours > self.bonus_threshold else 0
        total = base + bonus
        employee.log_transaction("payment", total, f"Hourly ({employee.hours} hours) + bonus ${bonus}")
        return total
