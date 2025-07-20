from .base_employee import Employee

class SalariedEmployee(Employee):
    def __init__(self, name, role, salary, vacation_policy, payment_policy):
        super().__init__(name, role, vacation_policy, payment_policy)
        self.salary = salary

   # def accept(self, visitor):  #VERIFICAR QUE SEA NECESARIO O NO LA IMPLEMENTACION DEL VISITOR
    #    return visitor.visit_salaried(self)
