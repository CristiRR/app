from .base_vacation import VacationPolicy

class DefaultVacationPolicy(VacationPolicy):
    def request_vacation(self, employee, days, payout):
        if employee.vacation_days < days:
            raise Exception("Not enough vacation days.")
        employee.vacation_days -= days
        employee.log_transaction("vacation", days, "Standard vacation/payout")
