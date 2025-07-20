from .base_employee import Employee

class Intern(Employee):
    def __init__(self, name, vacation_policy, payment_policy):
        super().__init__(name, "intern", vacation_policy, payment_policy)
        

   # def accept(self, visitor): # VERIFICAR QUE SEA NECESARIO O NO LA IMPLEMENTACION DEL VISITOR
      #  return visitor.visit_intern(self)

    def can_request_vacation(self) -> bool:
        return False
