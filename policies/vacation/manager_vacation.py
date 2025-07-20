from .base_vacation import VacationPolicy

class ManagerVacationPolicy(VacationPolicy):
    def request_vacation(self, employee, days, payout):
        if payout and days > 10:
            raise Exception("Managers can only request up to 10 days payout.")
       
        employee.vacation_days -= days
        employee.log_transaction("vacation", days, "Manager vacation/payout")
