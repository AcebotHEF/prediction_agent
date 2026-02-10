import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from data_loader import get_revenue_data
from forecast_prompt import forecast_template

# 1. Load Environment Variables (Securely loads GOOGLE_API_KEY)
load_dotenv()

def run_forecast_analysis():
    """
    Fetches revenue data and generates a forecast using Google Gemini.
    """
    try:
        # 2. Get the Data
        df = get_revenue_data()
        
        # Convert dataframe to string so the AI can read it
        revenue_table = df.to_string(index=False)
        
        # 3. Initialize Gemini
        # We use 'gemini-1.5-flash' for speed and cost efficiency.
        # You can change this to 'gemini-pro' if you need deeper reasoning.
        llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash", 
            temperature=0.3
        )
        
        # 4. Create the Chain (LCEL Syntax)
        # This pipes the prompt directly into the LLM
        chain = forecast_template | llm
        
        # 5. Invoke the Chain
        # We pass a dictionary matching the {revenue_table} variable in your prompt
        response = chain.invoke({"revenue_table": revenue_table})
        
        # Return the DataFrame (for the chart) and the AI's text (for the insight)
        return df, response.content

    except Exception as e:
        # Graceful error handling prevents the app from crashing
        return None, f"Error generating forecast: {str(e)}"