from .base_vacation import VacationPolicy

class ManagerVacationPolicy(VacationPolicy):
    def request_vacation(self, employee, days, payout):
        if payout and days > 10:
            raise Exception("El payout no puede exceder 10 días.")
        print(f"{employee.name} (Manager) solicita {days} días de vacaciones.")
        if payout:
            print(f"Payout solicitado por {days} días.")
        employee.log_transaction("vacation", days, "Manager vacation/payout")
