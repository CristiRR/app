from .base_employee import Employee

class Intern(Employee):
    def __init__(self, name, vacation_policy, payment_policy, salary=None, rate=None, hours=None):
        super().__init__(name, "intern", vacation_policy, payment_policy)
        self.salary = salary
        self.rate = rate
        self.hours = hours

    def can_request_vacation(self) -> bool:
        return False
