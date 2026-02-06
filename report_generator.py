from fpdf import FPDF
import pandas as pd
import matplotlib.pyplot as plt
import os


def generate_graphs(data):
    """Generate graphs and save as images"""

    # Revenue vs Expense vs Profit
    plt.figure()
    plt.plot(data["Month"], data["Revenue"], marker="o", label="Revenue")
    plt.plot(data["Month"], data["Expenses"], marker="o", label="Expenses")
    plt.plot(data["Month"], data["Profit"], marker="o", label="Profit")
    plt.title("Revenue vs Expenses vs Profit")
    plt.xlabel("Month")
    plt.ylabel("Amount (INR)")
    plt.legend()
    plt.tight_layout()
    plt.savefig("revenue_expense_profit.png")
    plt.close()

    # Cash Flow Bar Graph
    plt.figure()
    plt.bar(data["Month"], data["Cash Flow"])
    plt.title("Cash Flow Trend")
    plt.xlabel("Month")
    plt.ylabel("Cash Flow (INR)")
    plt.tight_layout()
    plt.savefig("cashflow.png")
    plt.close()


def generate_pdf_report(data, risk_obj, filename="Financial_Report.pdf"):

    data = data.copy()
    data["Profit"] = data["Revenue"] - data["Expenses"]
    data["Cash Flow"] = data["Revenue"] - (data["Expenses"] + data["Loan EMI"] + data["Tax Paid"])

    # Generate graphs
    generate_graphs(data)

    total_revenue = data["Revenue"].sum()
    total_expense = data["Expenses"].sum()
    total_profit = data["Profit"].sum()
    avg_profit_margin = (total_profit / total_revenue) * 100

    risk_level = risk_obj.final_risk_level()
    reasons = risk_obj.risk_explanation()
    recommendations = risk_obj.recommendations()

    investor_result = risk_obj.investor_score()
    loan_result = risk_obj.loan_eligibility()
    bankruptcy_result = risk_obj.bankruptcy_risk()
    fraud_result = risk_obj.fraud_detection()

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # ---------------- MAIN TITLE (ONLY ONCE) ----------------
    pdf.set_font("Arial", "B", 18)
    pdf.cell(0, 12, "AI Financial Health Report", ln=True, align="C")

    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, "SME Business Financial Analysis & Risk Report", ln=True, align="C")

    pdf.ln(8)

    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"Generated On: {pd.Timestamp.now()}", ln=True)
    pdf.ln(5)

    # ---------------- Financial Summary ----------------
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "1) Financial Summary", ln=True)

    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 8, f"Total Revenue: INR {total_revenue:,.0f}", ln=True)
    pdf.cell(0, 8, f"Total Expenses: INR {total_expense:,.0f}", ln=True)
    pdf.cell(0, 8, f"Total Profit: INR {total_profit:,.0f}", ln=True)
    pdf.cell(0, 8, f"Average Profit Margin: {avg_profit_margin:.2f}%", ln=True)

    pdf.ln(6)

    # ---------------- Risk Section ----------------
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "2) Risk Assessment", ln=True)

    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 8, f"Overall Risk Level: {risk_level}", ln=True)
    pdf.ln(3)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "Risk Explanation:", ln=True)

    pdf.set_font("Arial", "", 12)
    for r in reasons:
        pdf.set_x(pdf.l_margin)
        pdf.multi_cell(0, 7, f"- {r}")

    pdf.ln(5)

    # ---------------- Recommendations ----------------
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "3) AI Recommendations", ln=True)

    pdf.set_font("Arial", "", 12)
    for rec in recommendations:
        pdf.set_x(pdf.l_margin)
        pdf.multi_cell(0, 7, f"- {rec}")

    pdf.ln(5)

    # ---------------- Business Intelligence ----------------
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "4) Business Intelligence Results", ln=True)

    pdf.set_font("Arial", "", 12)

    pdf.set_x(pdf.l_margin)
    pdf.multi_cell(0, 8, f"Investor Decision: {investor_result}")

    pdf.set_x(pdf.l_margin)
    pdf.multi_cell(0, 8, f"Loan Eligibility: {loan_result}")

    pdf.set_x(pdf.l_margin)
    pdf.multi_cell(0, 8, f"Bankruptcy Prediction: {bankruptcy_result}")

    pdf.set_x(pdf.l_margin)
    pdf.multi_cell(0, 8, f"Fraud Detection: {fraud_result}")

    pdf.ln(6)

    # ---------------- Graph Section ----------------
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "5) Financial Graph Analysis", ln=True)
    pdf.ln(5)

    if os.path.exists("revenue_expense_profit.png"):
        pdf.image("revenue_expense_profit.png", x=15, w=180)
        pdf.ln(8)

    if os.path.exists("cashflow.png"):
        pdf.image("cashflow.png", x=15, w=180)
        pdf.ln(8)

    # ---------------- Table Section (NEW PAGE) ----------------
    pdf.add_page()

    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "6) Recent Financial Data (Last 5 Months)", ln=True)
    pdf.ln(5)

    recent = data.tail(5)

    headers = ["Month", "Revenue", "Expenses", "Profit", "Cash Flow"]
    col_widths = [25, 40, 40, 35, 45]

    # Table Header
    pdf.set_font("Arial", "B", 11)
    for i, h in enumerate(headers):
        pdf.cell(col_widths[i], 10, h, border=1, align="C")
    pdf.ln()

    # Table Rows
    pdf.set_font("Arial", "", 11)
    for _, row in recent.iterrows():
        pdf.cell(col_widths[0], 10, str(row["Month"]), border=1, align="C")
        pdf.cell(col_widths[1], 10, f"{row['Revenue']:,}", border=1, align="C")
        pdf.cell(col_widths[2], 10, f"{row['Expenses']:,}", border=1, align="C")
        pdf.cell(col_widths[3], 10, f"{row['Profit']:,}", border=1, align="C")
        pdf.cell(col_widths[4], 10, f"{row['Cash Flow']:,}", border=1, align="C")
        pdf.ln()

    pdf.ln(10)

    # ---------------- Conclusion ----------------
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "7) Final Conclusion", ln=True)

    pdf.set_font("Arial", "", 12)

    if risk_level == "LOW RISK":
        conclusion = "Business is financially stable. Focus on scaling, maintaining profit margin, and improving cash flow planning."
    elif risk_level == "MEDIUM RISK":
        conclusion = "Business is moderately stable. Expense control and receivable management are required for better stability."
    else:
        conclusion = "Business is under high risk. Immediate restructuring, cost optimization, and loan management is recommended."

    pdf.set_x(pdf.l_margin)
    pdf.multi_cell(0, 8, conclusion)

    pdf.output(filename)

    # Cleanup graph images
    if os.path.exists("revenue_expense_profit.png"):
        os.remove("revenue_expense_profit.png")

    if os.path.exists("cashflow.png"):
        os.remove("cashflow.png")

    return filename
