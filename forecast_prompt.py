# CHANGED: Use langchain_core to avoid import errors
from langchain_core.prompts import PromptTemplate

forecast_template = PromptTemplate.from_template("""
You are a financial forecasting analyst. Below is the monthly revenue data for the past 18 months:

{revenue_table}

Tasks:
1. Identify growth patterns or seasonality.
2. Forecast revenue for the next 3 months.
3. Provide actionable suggestions based on the forecast.

Respond in business-friendly language.
""")