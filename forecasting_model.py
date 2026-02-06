from sklearn.linear_model import LinearRegression
import numpy as np

class ForecastingModel:

    def __init__(self, data):
        self.data = data

    def predict_next_month(self):

        months = np.arange(len(self.data)).reshape(-1, 1)

        revenue = self.data["Revenue"].values
        expenses = self.data["Expenses"].values

        # Revenue model
        revenue_model = LinearRegression()
        revenue_model.fit(months, revenue)

        next_month = np.array([[len(self.data)]])
        predicted_revenue = revenue_model.predict(next_month)[0]

        # Expense model
        expense_model = LinearRegression()
        expense_model.fit(months, expenses)

        predicted_expense = expense_model.predict(next_month)[0]

        return round(predicted_revenue, 2), round(predicted_expense, 2)



