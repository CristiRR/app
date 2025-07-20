from abc import ABC, abstractmethod

class VacationPolicy(ABC):
    @abstractmethod 
    def request_vacation(self, employee, days: int, payout: bool): pass
