import random

class LiveFinancialAPI:

    def fetch_live_data(self):

        return {
            "revenue_today": random.randint(400000, 700000),
            "expenses_today": random.randint(250000, 450000),
            "transactions": random.randint(40, 120),
            "alerts": random.choice(["None", "Delay in payments", "High spending"])
        }
