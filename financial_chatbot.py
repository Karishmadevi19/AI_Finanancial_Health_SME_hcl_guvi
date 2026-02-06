class FinancialAdvisor:

    def get_advice(self, query):

        query = query.lower()

        if "profit" in query:
            return "Reduce operational expenses and improve pricing strategy."

        elif "loan" in query:
            return "Maintain strong cash flow and reduce existing liabilities."

        elif "risk" in query:
            return "Monitor expenses, loan EMI, and receivables."

        elif "investment" in query:
            return "Show revenue growth and positive cash flow to attract investors."

        else:
            return "Focus on revenue growth, cost optimization, and financial discipline."
