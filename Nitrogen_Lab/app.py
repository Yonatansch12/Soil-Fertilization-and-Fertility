import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("Nitrogen Fertilization Experiment")
st.write("This app displays results of nitrogen concentration changes over time for different soil treatments.")

# Example data (replace with actual data if available)
data = {
    "Days": [7, 14, 21],
    "Treatment_A": [5, 7, 8],
    "Treatment_B": [15, 25, 30],
    "Treatment_C": [10, 18, 22]
}
df = pd.DataFrame(data)

# Interactive Plot
st.subheader("Interactive Visualization")
fig = px.line(
    df,
    x="Days",
    y=["Treatment_A", "Treatment_B", "Treatment_C"],
    title="Nitrogen Concentration Over Time",
    labels={"value": "Concentration (mg/kg)", "variable": "Treatment"}
)
st.plotly_chart(fig)

# Display Data Table
st.subheader("Data Table")
st.write(df)

# Insights Section
st.subheader("Insights")
st.write("""
- **Treatment B** shows the fastest increase in nitrogen concentration over the 21 days.
- **Treatment C** shows a moderate but steady increase.
- **Treatment A** remains low and stable, indicating minimal nitrogen availability.
""")
