import os
import pandas as pd
from langchain_google_genai import ChatGoogleGenerativeAI  # <--- CHANGED
from data_loader import get_revenue_data
from forecast_prompt import forecast_template

# Ensure your key is set (if not already set in your environment)
# os.environ["GOOGLE_API_KEY"] = "your_google_api_key_here"

def run_forecast_analysis():
    df = get_revenue_data()
    revenue_table = df.to_string(index=False)
    
    prompt = forecast_template.format(revenue_table=revenue_table)
    
    # CHANGED: Using Google Gemini instead of OpenAI
    llm = ChatGoogleGenerativeAI(
        model="models/gemini-2.0-flash",  # Using the model we confirmed works
        temperature=0.3
    )
    
    # CHANGED: .predict() is deprecated. We use .invoke().content
    response = llm.invoke(prompt)
    forecast_summary = response.content
    
    return df, forecast_summary
