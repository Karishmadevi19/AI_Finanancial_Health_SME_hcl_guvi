class HealthScoreCalculator:
    def __init__(self, data):
        self.data = data

    def calculate_score(self):
        revenue_avg = self.data["Revenue"].mean()
        expense_avg = self.data["Expenses"].mean()
        loan_avg = self.data["Loan EMI"].mean()

        score = 100

        # Expense ratio impact
        if expense_avg > 0.7 * revenue_avg:
            score -= 20
        elif expense_avg > 0.5 * revenue_avg:
            score -= 10

        # Loan burden impact
        if loan_avg > 0.3 * revenue_avg:
            score -= 15

        return max(score, 0)
