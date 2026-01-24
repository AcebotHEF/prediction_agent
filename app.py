import streamlit as st
import matplotlib.pyplot as plt
from forecast_agent import run_forecast_analysis

st.title("📊 Advanced Prediction Agent")

if st.button("Run Forecast"):
    # Add a spinner so the user knows AI is working
    with st.spinner("Analyzing data and generating forecast..."):
        try:
            df, summary = run_forecast_analysis()

            # Line Chart with better formatting
            st.subheader("📈 Revenue Over Time")
            
            # Create a larger figure size
            fig, ax = plt.subplots(figsize=(10, 5))
            
            # Plot with styling
            ax.plot(df["Month"], df["Revenue"], marker='o', linestyle='-', color='#4CAF50')
            ax.set_xlabel("Month")
            ax.set_ylabel("Revenue")
            ax.set_title("Historical Revenue Trend (18 Months)")
            
            # Rotate x-axis labels so they don't overlap
            plt.xticks(rotation=45)
            plt.tight_layout()
            
            st.pyplot(fig)

            # Summary
            st.subheader("🧠 AI Forecast Summary")
            st.markdown(summary)  # Use markdown to render bold text from the AI

        except Exception as e:
            st.error(f"An error occurred: {e}")

# To run this app, use the command:
# python -m streamlit run app.py