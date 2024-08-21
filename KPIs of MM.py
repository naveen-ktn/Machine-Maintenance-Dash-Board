import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set up the Streamlit app
st.title("Downtime Causes and Mitigation Strategies Dashboard")

# Sidebar for user input
st.sidebar.header("Input Parameters")

# Define downtime causes and their corresponding percentages
downtime_data = {
    "Cause": [
        "Hardware Failures",
        "Software Issues",
        "Human Error",
        "Planned Maintenance",
        "Network Issues",
        "Security Incidents",
        "Environmental Factors",
        "Supply Chain Issues",
        "Operational Bottlenecks",
        "Third-Party Dependencies"
    ],
    "Percentage": [30, 20, 15, 10, 10, 5, 5, 2, 2, 1]
}

# Create a DataFrame
df = pd.DataFrame(downtime_data)

# Display the data
st.subheader("Downtime Causes with Percentages")
st.write(df)

# Plot a pie chart for downtime causes
st.subheader("Downtime Causes Distribution")
fig, ax = plt.subplots()
ax.pie(df["Percentage"], labels=df["Cause"], autopct='%1.1f%%', startangle=140)
ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
st.pyplot(fig)

# Corresponding mitigation strategies for each cause
mitigation_strategies = {
    "Hardware Failures": "Preventive maintenance, system upgrades, power management, cooling systems",
    "Software Issues": "Regular updates, thorough testing, data integrity measures",
    "Human Error": "Training, SOPs, automation",
    "Planned Maintenance": "Minimize downtime, predictive maintenance, clear communication",
    "Network Issues": "Redundancy, bandwidth management, DNS management",
    "Security Incidents": "Cybersecurity protocols, access control, incident response plan",
    "Environmental Factors": "Disaster recovery plan, protective measures, geographic considerations",
    "Supply Chain Issues": "Diversify suppliers, inventory management, logistics planning",
    "Operational Bottlenecks": "Process optimization, resource allocation, continuous improvement",
    "Third-Party Dependencies": "SLAs, backup providers, monitoring and alerts"
}

# Display the mitigation strategies
st.subheader("Mitigation Strategies")
selected_cause = st.selectbox("Select a Downtime Cause to view its Mitigation Strategies", df["Cause"])

if selected_cause:
    st.write(f"**Mitigation Strategies for {selected_cause}:**")
    st.write(mitigation_strategies[selected_cause])

# Footer
st.sidebar.markdown("---")
st.sidebar.write("This dashboard visualizes the causes of downtime and provides strategies to overcome them.")
