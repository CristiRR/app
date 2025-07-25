from models.salaried import SalariedEmployee
from models.hourly import HourlyEmployee
from models.freelancer import Freelancer
from models.intern import Intern
from policies.vacation.manager_vacation import ManagerVacationPolicy
from policies.vacation.vp_vacation import VPVacationPolicy
from policies.vacation.intern_vacation import InternVacationPolicy
from policies.vacation.freelancer_vacation import FreelancerVacationPolicy
from policies.vacation.default_vacation import DefaultVacationPolicy
from policies.payment.intern_payment import InternPaymentPolicy

class EmployeeFactory:
    def __init__(self, policies):
        self.policies = policies

    def create_employee(self, name, role, emp_type, tipo_pago=None):
        if emp_type == "salaried":
            salary = float(input("Salario mensual: "))
            vac_policy = self._get_vacation_policy(role)
            return SalariedEmployee(name, role, salary, vac_policy, self.policies["salaried"])

        elif emp_type == "hourly":
            rate = float(input("Tarifa por hora: "))
            hours = int(input("Horas trabajadas: "))
            vac_policy = self._get_vacation_policy(role)
            return HourlyEmployee(name, role, rate, hours, vac_policy, self.policies["hourly"])

        elif emp_type == "freelancer":
            projects = []
            while True:
                pname = input("Nombre del proyecto (o 'fin' para terminar): ")
                if pname.lower() == "fin":
                    break
                amount = float(input("Monto del proyecto: "))
                projects.append({"name": pname, "amount": amount})
            return Freelancer(name, projects, DefaultVacationPolicy(), self.policies["freelancer"])

        elif emp_type == "intern":
            if tipo_pago == "salaried":
                salary = float(input("Salario mensual del intern: "))
                return Intern(name, InternVacationPolicy(), self.policies["intern"], salary=salary)
            elif tipo_pago == "hourly":
                rate = float(input("Tarifa por hora del intern: "))
                hours = int(input("Horas trabajadas por el intern: "))
                return Intern(name, InternVacationPolicy(), self.policies["intern"], rate=rate, hours=hours)
            else:
                raise ValueError("Tipo de pago para intern no válido.")

        else:
            raise ValueError("Tipo de empleado no válido.")

    def _get_vacation_policy(self, role):
        policies = {
            "manager": ManagerVacationPolicy(),
            "vice_president": VPVacationPolicy(),
            "intern": InternVacationPolicy(),
            "freelancer": FreelancerVacationPolicy()
        }
        return policies.get(role, DefaultVacationPolicy())
