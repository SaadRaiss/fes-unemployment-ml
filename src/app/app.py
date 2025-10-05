import streamlit as st

st.set_page_config(page_title="Fes Unemployment", layout="wide")
st.title("Fes Unemployment – ML Prediction & Monitoring")
st.write("Quick demo. See README and the notebook for details.")

col1, col2, col3 = st.columns(3)
col1.metric("Current Rate (%)", "17.32", delta="2.9")
col2.metric("Risk Score", "0.411", delta="-0.089")
col3.metric("System Health", "0.95")

st.divider()
st.subheader("Executive Dashboard Preview")
try:
    st.image("assets/dashboard_overview.png", use_column_width=True)
except Exception:
    st.info("Add a screenshot as assets/dashboard_overview.png")
