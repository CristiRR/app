from .base_employee import Employee

class HourlyEmployee(Employee):
    def __init__(self, name, role, rate, hours, vacation_policy, payment_policy):
        super().__init__(name, role, vacation_policy, payment_policy)
        self.rate = rate
        self.hours = hours

  #  def accept(self, visitor): # VERIFICAR QUE SEA NECESARIO O NO LA IMPLEMENTACION DEL VISITOR
   #     return visitor.visit_hourly(self)
