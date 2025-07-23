from abc import ABC, abstractmethod
from typing import List
from datetime import datetime

class Employee(ABC):
    def __init__(self, name, role, vacation_policy, payment_policy): 
        self.name = name
        self.role = role
        self.vacation_policy = vacation_policy
        self.payment_policy = payment_policy
        self.transactions: List[dict] = []

    def request_vacation(self, days: int, payout: bool):
        self.vacation_policy.request_vacation(self, days, payout)

    def calculate_payment(self):
        return self.payment_policy.calculate_payment(self)

    

    def log_transaction(self, type_op, amount, description):
        self.transactions.append({
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": type_op,
            "amount": amount,
            "description": description
        })

    def show_transactions(self):
        print(f"--- Historial de transacciones de {self.name} ---")
        for t in sorted(self.transactions, key=lambda x: x["date"], reverse=True):
            print(f"{t['date']} | {t['type']} | ${t['amount']} | {t['description']}")

    def can_request_vacation(self) -> bool:
        return True
