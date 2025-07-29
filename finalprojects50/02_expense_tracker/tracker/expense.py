

from datetime import datetime

class Expense:
    def __init__(self, amount, category, date):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Amount must be a positive number.")
        try:
            self.date = datetime.strptime(date, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format.")
        
        self.amount = float(amount)
        self.category = category.capitalize()

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "date": self.date.strftime("%Y-%m-%d")
        }

    @staticmethod
    def from_dict(data):
        return Expense(
            float(data["amount"]),
            data["category"],
            data["date"]
        )

    def __str__(self):
        return f"{self.date} | ₹{self.amount:,.2f} | {self.category}"
