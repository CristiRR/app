from .base_vacation import VacationPolicy

class InternVacationPolicy(VacationPolicy):
    def request_vacation(self, employee, days, payout):
        raise Exception("Interns cannot take vacations or payouts.")
