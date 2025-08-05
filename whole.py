import streamlit as st

st.set_page_config(page_title="Earned Value Calculator", layout="centered")

st.title("📊 Earned Value Management (EVM) Calculator")

st.markdown("Enter the project parameters below:")

# Input Fields (Months instead of days)
project_duration = st.number_input("Project Duration (in months)", min_value=1)
elapsed_time = st.number_input("Elapsed Time (in months)", min_value=0, max_value=project_duration)

planned_percent = st.slider("Planned % Complete", min_value=0, max_value=100)
actual_percent = st.slider("Actual % Complete", min_value=0, max_value=100)
actual_cost = st.number_input("Actual Cost (AC)", min_value=0.0, step=100.0)
bac = st.number_input("Budget at Completion (BAC)", min_value=0.0, step=100.0)

# Calculate Metrics
if st.button("Calculate"):
    # Calculations
    planned_value = (planned_percent / 100) * bac
    earned_value = (actual_percent / 100) * bac
    schedule_variance = earned_value - planned_value
    cost_variance = earned_value - actual_cost

    # Results
    st.subheader("📈 Results")
    st.write(f"**Earned Value (EV)**: ₹{earned_value:,.2f}")
    st.write(f"**Planned Value (PV)**: ₹{planned_value:,.2f}")
    st.write(f"**Schedule Variance (SV = EV - PV)**: ₹{schedule_variance:,.2f}")
    st.write(f"**Cost Variance (CV = EV - AC)**: ₹{cost_variance:,.2f}")

    # Insights
    st.subheader("🔍 Insights")

    st.markdown("**Schedule Variance (SV):**")
    if schedule_variance > 0:
        st.success("✅ You are **ahead of schedule**.")
    elif schedule_variance < 0:
        st.error("⏳ You are **behind schedule**.")
    else:
        st.info("🟦 You are **on schedule**.")

    st.markdown("**Cost Variance (CV):**")
    if cost_variance > 0:
        st.success("✅ You are **under budget**.")
    elif cost_variance < 0:
        st.error("💰 You are **over budget**.")
    else:
        st.info("🟦 You are **on budget**.")
