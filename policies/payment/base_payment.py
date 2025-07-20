from abc import ABC, abstractmethod

class PaymentPolicy(ABC):
    @abstractmethod
    def calculate_payment(self, employee): pass
