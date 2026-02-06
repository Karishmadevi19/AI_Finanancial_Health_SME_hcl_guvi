import numpy as np

class RiskDetector:

    def __init__(self, data):
        self.data = data

    # Rule-based risk
    def rule_based_risk(self):

        revenue_avg = self.data["Revenue"].mean()
        expense_avg = self.data["Expenses"].mean()
        loan_avg = self.data["Loan EMI"].mean()

        risk_score = 0

        if expense_avg > 0.7 * revenue_avg:
            risk_score += 1

        if loan_avg > 0.3 * revenue_avg:
            risk_score += 1

        if self.data["Payables"].mean() > self.data["Receivables"].mean():
            risk_score += 1

        return risk_score

    # ML-inspired scoring
    def ml_risk_score(self):

        cash_flow = self.data["Revenue"] - self.data["Expenses"]
        volatility = np.std(cash_flow)

        if volatility > 50000:
            return 2
        elif volatility > 25000:
            return 1
        else:
            return 0

    # Final risk level
    def final_risk_level(self):

        total = self.rule_based_risk() + self.ml_risk_score()

        if total >= 3:
            return "HIGH RISK"
        elif total == 2:
            return "MEDIUM RISK"
        else:
            return "LOW RISK"

    # 🧠 NEW: Risk Explanation Engine
    def risk_explanation(self):

        reasons = []

        if self.data["Expenses"].mean() > 0.7 * self.data["Revenue"].mean():
            reasons.append("High operational expenses")

        if self.data["Loan EMI"].mean() > 0.3 * self.data["Revenue"].mean():
            reasons.append("Heavy loan burden")

        if self.data["Payables"].mean() > self.data["Receivables"].mean():
            reasons.append("More payables than receivables")

        cash_flow = self.data["Revenue"] - self.data["Expenses"]

        if np.std(cash_flow) > 25000:
            reasons.append("Unstable cash flow")

        if not reasons:
            reasons.append("Stable financial performance")

        return reasons

    # 🤖 NEW: AI Recommendation Engine
    def recommendations(self):

        suggestions = []

        if self.data["Expenses"].mean() > 0.7 * self.data["Revenue"].mean():
            suggestions.append("Reduce operational expenses")

        if self.data["Loan EMI"].mean() > 0.3 * self.data["Revenue"].mean():
            suggestions.append("Restructure or refinance loans")

        if self.data["Payables"].mean() > self.data["Receivables"].mean():
            suggestions.append("Improve receivable collection")

        cash_flow = self.data["Revenue"] - self.data["Expenses"]

        if np.std(cash_flow) > 25000:
            suggestions.append("Stabilize cash flow planning")

        if not suggestions:
            suggestions.append("Business financially stable — consider expansion")

        return suggestions

    # 💼 Investor Decision AI
    def investor_score(self):

        revenue_growth = self.data["Revenue"].pct_change().mean()
        expense_ratio = self.data["Expenses"].mean() / self.data["Revenue"].mean()
        cash_flow = (self.data["Revenue"] - self.data["Expenses"]).mean()

        score = 0

        if revenue_growth > 0:
            score += 1

        if expense_ratio < 0.7:
            score += 1

        if cash_flow > 0:
            score += 1

        if score == 3:
            return "STRONG INVESTMENT OPPORTUNITY"
        elif score == 2:
            return "MODERATE INVESTMENT OPPORTUNITY"
        else:
            return "HIGH INVESTMENT RISK"

    # 🏦 Loan Eligibility Predictor
    def loan_eligibility(self):

        revenue_avg = self.data["Revenue"].mean()
        loan_avg = self.data["Loan EMI"].mean()
        profit = (self.data["Revenue"] - self.data["Expenses"]).mean()

        if profit > 0 and loan_avg < 0.4 * revenue_avg:
            return "ELIGIBLE FOR BUSINESS LOAN"

        elif profit > 0:
            return "LOAN POSSIBLE WITH CONDITIONS"

        else:
            return "HIGH LOAN REJECTION RISK"
    

        # 📉 Bankruptcy Prediction AI
    def bankruptcy_risk(self):

        profit = (self.data["Revenue"] - self.data["Expenses"]).mean()
        expense_ratio = self.data["Expenses"].mean() / self.data["Revenue"].mean()
        loan_pressure = self.data["Loan EMI"].mean() / self.data["Revenue"].mean()

        risk_score = 0

        if profit < 0:
            risk_score += 2

        if expense_ratio > 0.8:
            risk_score += 1

        if loan_pressure > 0.5:
            risk_score += 1

        if risk_score >= 3:
            return "HIGH BANKRUPTCY RISK"
        elif risk_score == 2:
            return "MODERATE BANKRUPTCY RISK"
        else:
            return "LOW BANKRUPTCY RISK"



        # 🕵 Fraud Detection AI
    def fraud_detection(self):

        revenue_change = self.data["Revenue"].pct_change().abs().max()
        expense_spike = self.data["Expenses"].pct_change().abs().max()
        tax_variation = self.data["Tax Paid"].std()

        if revenue_change > 0.4 or expense_spike > 0.4:
            return "POSSIBLE FINANCIAL MANIPULATION DETECTED"

        elif tax_variation > 10000:
            return "TAX IRREGULARITY DETECTED"

        else:
            return "NO FRAUD SIGNALS"


