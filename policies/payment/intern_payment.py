from .base_payment import PaymentPolicy


class InternPaymentPolicy(PaymentPolicy):
    def calculate_payment(self, employee):
        if employee.salary is not None:
            amount = employee.salary
        elif employee.rate is not None and employee.hours is not None:
            amount = employee.rate * employee.hours
        else:
            amount = 0
        employee.log_transaction("payment", amount, "Intern payment (sin bonus)")
        return amount