from .base_vacation import VacationPolicy

class FreelancerVacationPolicy(VacationPolicy):
    def request_vacation(self, employee, days, payout):
        raise Exception("Freelancers no pueden tomar vacaciones ni recibir payout.")
