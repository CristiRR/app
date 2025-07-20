from .base_payment import PaymentPolicy

class SalariedPaymentPolicy(PaymentPolicy):
    def __init__(self, bonus_percent=0.10):
        self.bonus_percent = bonus_percent

    def calculate_payment(self, employee):
        bonus = employee.salary * self.bonus_percent
        total = employee.salary + bonus
        employee.log_transaction("payment", total, f"Salaried + {self.bonus_percent*100:.0f}% bonus")
        return total
