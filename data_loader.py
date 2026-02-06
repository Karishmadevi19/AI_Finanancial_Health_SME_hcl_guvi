import pandas as pd

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        try:
            print(f"Trying to load file from: {self.file_path}")
            self.data = pd.read_csv(self.file_path)
            print("Data loaded successfully.")
        except Exception as e:
            print("Error loading data:", e)

    def validate_data(self):
        required_columns = [
            "Revenue",
            "Expenses",
            "Inventory",
            "Receivables",
            "Payables",
            "Loan EMI",
            "Tax Paid"
        ]

        for col in required_columns:
            if col not in self.data.columns:
                print(f"Missing column: {col}")
                return False

        print("Data validation successful.")
        return True
