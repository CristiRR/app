from .base_vacation import VacationPolicy

class VPVacationPolicy(VacationPolicy):
    def request_vacation(self, employee, days, payout):
        if days > 5:
            raise Exception("No puede solicitar más de 5 días por vez.")
        employee.log_transaction("vacation", days, "VP vacation/payout")
