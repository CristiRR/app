from .base_employee import Employee

class Freelancer(Employee):
    def __init__(self, name, projects, vacation_policy, payment_policy):
        super().__init__(name, "freelancer", vacation_policy, payment_policy)
        self.projects = projects

    #def accept(self, visitor): # VERIFICAR QUE SEA NECESARIO O NO LA IMPLEMENTACION DEL VISITOR
       # return visitor.visit_freelancer(self)

    def can_request_vacation(self) -> bool:
        return False
