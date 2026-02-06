import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

from risk_detection import RiskDetector
from final_detection import FinalFinancialAdvisor
from report_generator import generate_pdf_report


# ------------------- Page Config -------------------
st.set_page_config(page_title="AI Financial Health SME", layout="wide")


# ------------------- CUSTOM CSS (PRO UI) -------------------
st.markdown("""
<style>
    .main {
        background-color: #0e1117;
        color: white;
    }
    .block-container {
        padding-top: 1.5rem;
    }
    .title-text {
        font-size: 42px;
        font-weight: 900;
        text-align: center;
        color: #00d4ff;
        margin-bottom: 5px;
    }
    .subtitle-text {
        text-align: center;
        font-size: 18px;
        color: #b0b0b0;
        margin-bottom: 25px;
    }
    .card {
        background: linear-gradient(135deg, #1f1f2e, #2a2a40);
        padding: 20px;
        border-radius: 18px;
        box-shadow: 0px 4px 18px rgba(0, 0, 0, 0.55);
        text-align: center;
        color: white;
    }
    .card h2 {
        font-size: 16px;
        margin-bottom: 5px;
        color: #00ffcc;
        font-weight: 700;
    }
    .card h1 {
        font-size: 30px;
        margin: 0;
        color: white;
        font-weight: 900;
    }
    .section-title {
        font-size: 24px;
        font-weight: 800;
        color: #00ffcc;
        margin-top: 10px;
        margin-bottom: 10px;
    }
    .risk-low {
        background-color: #00c853;
        color: white;
        padding: 8px 16px;
        border-radius: 12px;
        font-weight: bold;
        display: inline-block;
    }
    .risk-medium {
        background-color: #ff9100;
        color: white;
        padding: 8px 16px;
        border-radius: 12px;
        font-weight: bold;
        display: inline-block;
    }
    .risk-high {
        background-color: #d50000;
        color: white;
        padding: 8px 16px;
        border-radius: 12px;
        font-weight: bold;
        display: inline-block;
    }
</style>
""", unsafe_allow_html=True)


# ------------------- HEADER -------------------
st.markdown("<div class='title-text'>📊 AI Financial Health Monitoring Dashboard</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle-text'>Smart Financial Analytics • Risk Detection • AI Business Advisor • PDF Report</div>",
            unsafe_allow_html=True)


# ------------------- Load Dataset -------------------
@st.cache_data
def load_data():
    df = pd.read_csv("dataset/sme_financial_data.csv")
    return df


data = load_data()

# Derived metrics
data["Profit"] = data["Revenue"] - data["Expenses"]
data["Cash Flow"] = data["Revenue"] - (data["Expenses"] + data["Loan EMI"] + data["Tax Paid"])


# ------------------- SIDEBAR -------------------
st.sidebar.title("⚙ Dashboard Settings")

company_name = st.sidebar.text_input("Company Name", "SME Business")
selected_month = st.sidebar.selectbox("Select Month", data["Month"].unique())
month_data = data[data["Month"] == selected_month].iloc[0]


st.sidebar.markdown("---")
st.sidebar.info("💡 Ask AI questions like:\n\n"
                "- How can I improve profit?\n"
                "- Am I eligible for loan?\n"
                "- Predict next month revenue\n"
                "- What is my risk level?")


# ------------------- KPI CARDS -------------------

selected_revenue = int(month_data["Revenue"])
selected_expenses = int(month_data["Expenses"])
selected_profit = int(month_data["Profit"])
selected_cashflow = int(month_data["Cash Flow"])
selected_inventory = int(month_data["Inventory"])

st.markdown(f"<div class='section-title'>📌 KPIs for {selected_month}</div>", unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown(f"""
        <div class="card">
            <h2>Revenue</h2>
            <h1>₹{selected_revenue:,}</h1>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="card">
            <h2>Expenses</h2>
            <h1>₹{selected_expenses:,}</h1>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="card">
            <h2>Profit</h2>
            <h1>₹{selected_profit:,}</h1>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
        <div class="card">
            <h2>Cash Flow</h2>
            <h1>₹{selected_cashflow:,}</h1>
        </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown(f"""
        <div class="card">
            <h2>Inventory</h2>
            <h1>₹{selected_inventory:,}</h1>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.info(f"📌 You are currently viewing **{selected_month}** financial snapshot.")


# ------------------- Risk Detection -------------------
risk = RiskDetector(data)
risk_level = risk.final_risk_level()

if risk_level == "LOW RISK":
    badge = "<span class='risk-low'>LOW RISK</span>"
elif risk_level == "MEDIUM RISK":
    badge = "<span class='risk-medium'>MEDIUM RISK</span>"
else:
    badge = "<span class='risk-high'>HIGH RISK</span>"

st.markdown(f"## 📌 Overall Business Risk: {badge}", unsafe_allow_html=True)

st.markdown("---")


# ------------------- TABS -------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Dashboard",
    "⚠ Risk Analysis",
    "💼 Business Intelligence",
    "🤖 AI Advisor",
    "📄 Report & Dataset"
])


# ------------------- TAB 1 : DASHBOARD -------------------
with tab1:
    st.markdown("<div class='section-title'>📈 Revenue vs Expenses vs Profit</div>", unsafe_allow_html=True)

    fig, ax = plt.subplots()
    ax.plot(data["Month"], data["Revenue"], marker="o", label="Revenue")
    ax.plot(data["Month"], data["Expenses"], marker="o", label="Expenses")
    ax.plot(data["Month"], data["Profit"], marker="o", label="Profit")
    ax.set_xlabel("Month")
    ax.set_ylabel("Amount (₹)")
    ax.legend()
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)

    st.markdown("<div class='section-title'>💰 Cash Flow Trend</div>", unsafe_allow_html=True)

    fig2, ax2 = plt.subplots()
    ax2.bar(data["Month"], data["Cash Flow"])
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Cash Flow (₹)")
    ax2.grid(True, axis="y", alpha=0.3)
    st.pyplot(fig2)

    st.markdown("<div class='section-title'>📦 Inventory Trend</div>", unsafe_allow_html=True)

    fig3, ax3 = plt.subplots()
    ax3.plot(data["Month"], data["Inventory"], marker="o", label="Inventory")
    ax3.set_xlabel("Month")
    ax3.set_ylabel("Inventory (₹)")
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    st.pyplot(fig3)

    st.markdown("<div class='section-title'>📊 Receivables vs Payables</div>", unsafe_allow_html=True)

    fig4, ax4 = plt.subplots()
    ax4.plot(data["Month"], data["Receivables"], marker="o", label="Receivables")
    ax4.plot(data["Month"], data["Payables"], marker="o", label="Payables")
    ax4.set_xlabel("Month")
    ax4.set_ylabel("Amount (₹)")
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    st.pyplot(fig4)


# ------------------- TAB 2 : RISK ANALYSIS -------------------
with tab2:
    st.markdown("<div class='section-title'>⚠ Risk Explanation</div>", unsafe_allow_html=True)

    if risk_level == "HIGH RISK":
        st.error(f"🚨 {risk_level}")
    elif risk_level == "MEDIUM RISK":
        st.warning(f"⚠️ {risk_level}")
    else:
        st.success(f"✅ {risk_level}")

    for reason in risk.risk_explanation():
        st.write("🔹", reason)

    st.markdown("<div class='section-title'>🤖 AI Recommendations</div>", unsafe_allow_html=True)

    for rec in risk.recommendations():
        st.write("✅", rec)

    st.markdown("<div class='section-title'>📊 Risk Meter</div>", unsafe_allow_html=True)

    risk_map = {"LOW RISK": 1, "MEDIUM RISK": 2, "HIGH RISK": 3}
    value = risk_map[risk_level]

    fig5, ax5 = plt.subplots()
    ax5.bar(["Risk Score"], [value])
    ax5.set_ylim(0, 3)
    ax5.set_ylabel("Risk Scale (1-3)")
    ax5.grid(True, axis="y", alpha=0.3)
    st.pyplot(fig5)


# ------------------- TAB 3 : BUSINESS INTELLIGENCE -------------------
with tab3:
    st.markdown("<div class='section-title'>🏦 Loan Eligibility Prediction</div>", unsafe_allow_html=True)

    loan_result = risk.loan_eligibility()
    if "ELIGIBLE" in loan_result:
        st.success(loan_result)
    elif "CONDITIONS" in loan_result:
        st.warning(loan_result)
    else:
        st.error(loan_result)

    st.markdown("<div class='section-title'>📉 Bankruptcy Risk Prediction</div>", unsafe_allow_html=True)

    bankruptcy = risk.bankruptcy_risk()
    if "HIGH" in bankruptcy:
        st.error(bankruptcy)
    elif "MODERATE" in bankruptcy:
        st.warning(bankruptcy)
    else:
        st.success(bankruptcy)

    st.markdown("<div class='section-title'>🕵 Fraud Detection AI</div>", unsafe_allow_html=True)

    fraud = risk.fraud_detection()
    if "NO" in fraud:
        st.success(fraud)
    else:
        st.error(fraud)

    st.markdown("<div class='section-title'>💼 Investor Intelligence</div>", unsafe_allow_html=True)

    investor_result = risk.investor_score()
    if "STRONG" in investor_result:
        st.success(investor_result)
    elif "MODERATE" in investor_result:
        st.warning(investor_result)
    else:
        st.error(investor_result)


# ------------------- TAB 4 : AI ADVISOR -------------------
with tab4:
    st.markdown("<div class='section-title'>🤖 AI Financial Advisor (Gemini Powered)</div>", unsafe_allow_html=True)

    advisor = FinalFinancialAdvisor(data)

    user_query = st.text_input("Ask a business question (Example: How can I improve profit margin?)")

    if st.button("💬 Ask AI Advisor"):
        if user_query.strip() == "":
            st.warning("⚠ Please type a question first.")
        else:
            response = advisor.get_advice(user_query)
            st.success("✅ AI Response Generated")
            st.write(response)


# ------------------- TAB 5 : REPORT + DATASET -------------------
with tab5:
    st.markdown("<div class='section-title'>📄 Generate Financial Report (PDF)</div>", unsafe_allow_html=True)

    if st.button("📌 Generate PDF Report"):
        file_name = generate_pdf_report(data, risk)

        with open(file_name, "rb") as f:
            st.download_button(
                label="📥 Download Financial Report PDF",
                data=f,
                file_name="Financial_Report.pdf",
                mime="application/pdf"
            )

        st.success("✅ PDF Report Generated Successfully!")

    st.markdown("---")

    st.markdown("<div class='section-title'>📌 SME Financial Dataset</div>", unsafe_allow_html=True)

    st.dataframe(data, use_container_width=True)

    st.markdown("<div class='section-title'>📌 Selected Month Details</div>", unsafe_allow_html=True)

    selected_data = data[data["Month"] == selected_month]
    st.table(selected_data)


# ------------------- FOOTER -------------------
st.markdown("---")
st.markdown("💡 **Developed for HCL Quvi Hackathon | AI Financial Health SME Project**")
