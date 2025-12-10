import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt

# -----------------------------
# Sample Data Setup
# -----------------------------
months = pd.date_range("2025-01-01", periods=12, freq="M")
subscribers = np.linspace(500, 1000, 12).astype(int)
arpu = 600
mrr = subscribers * arpu
install_fees = np.random.randint(20000, 40000, 12)
total_revenue = mrr + install_fees

bandwidth = 150000
staff = 100000
maintenance = 50000
marketing = 50000
total_costs = bandwidth + staff + maintenance + marketing
costs = [total_costs] * 12
net_profit = total_revenue - costs

# -----------------------------
# Streamlit Dashboard Layout
# -----------------------------
st.title("📊 ISP Financial Projection Dashboard")

# KPI Cards
col1, col2, col3, col4 = st.columns(4)
col1.metric("Active Subscribers", subscribers[-1])
col2.metric("ARPU (₹)", arpu)
col3.metric("Monthly Revenue (₹)", int(total_revenue[-1]))
col4.metric("Net Profit (₹)", int(net_profit[-1]))

# Line Chart: MRR
st.subheader("Monthly Recurring Revenue (MRR)")
st.line_chart(pd.DataFrame({"MRR": mrr}, index=months))

# Line Chart: Subscriber Growth
st.subheader("Subscriber Growth")
st.line_chart(pd.DataFrame({"Subscribers": subscribers}, index=months))

# Bar Chart: New vs Disconnections
new_connections = np.random.randint(30, 60, 12)
disconnections = np.random.randint(10, 20, 12)
st.subheader("New Connections vs Disconnections")
df_conn = pd.DataFrame({"New": new_connections, "Disconnections": disconnections}, index=months)
st.bar_chart(df_conn)

# Pie Chart: Cost Distribution
st.subheader("Operating Cost Distribution")
fig = go.Figure(go.Pie(labels=['Bandwidth','Staff','Maintenance','Marketing'],
                       values=[bandwidth, staff, maintenance, marketing],
                       hole=0.4))
st.plotly_chart(fig)

# Net Profit Line
st.subheader("Net Profit Over Time")
st.line_chart(pd.DataFrame({"Net Profit": net_profit}, index=months))

# Projected Growth Area Chart
st.subheader("Projected MRR Growth (Months 13–24)")
future_subs = np.linspace(1000, 1500, 12).astype(int)
future_mrr = future_subs * arpu
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=np.arange(13,25), y=future_mrr, fill='tozeroy'))
fig2.update_layout(title="Projected MRR Growth", xaxis_title="Month", yaxis_title="Revenue (₹)")
st.plotly_chart(fig2)
