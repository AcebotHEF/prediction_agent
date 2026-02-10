# 📈 Agent #3: Advanced Prediction Agent

**A Financial Forecasting AI driven by OpenAI & LangChain.**

[Image of financial forecasting chart]

## 📌 Overview
The **Advanced Prediction Agent** is a specialized tool for analyzing time-series financial data. Unlike traditional statistical models that only look at numbers, this agent uses **Large Language Models (LLMs)** to interpret trends, identify seasonality, and generate qualitative strategic advice alongside quantitative forecasts.

In this lab, we simulate 18 months of revenue data and use **OpenAI (GPT-3.5/4)** to predict future performance and visualize the trajectory.

## 🚀 Features
* **Time-Series Generation:** Creates realistic mock revenue data with growth trends and noise.
* **AI Forecasting:** Uses GPT to analyze 18-month historical data and predict the next quarter.
* **Trend Analysis:** Identifies growth patterns and potential seasonality automatically.
* **Visual Dashboard:** Renders interactive matplotlib line charts within a Streamlit interface.

## 🛠️ Tech Stack
* **Frontend:** Streamlit
* **AI Logic:** LangChain (Prompt Templates & Chains)
* **Model:** OpenAI GPT-3.5 Turbo (or GPT-4)
* **Data Science:** Pandas & NumPy
* **Visualization:** Matplotlib
* **Language:** Python 3.10+

## 📂 Project Structure

```text
prediction_agent/
├── app.py              # Main Streamlit Dashboard
├── forecast_agent.py   # AI Logic (LangChain integration)
├── forecast_prompt.py  # Prompt Engineering for Financial Analyst Persona
├── data_loader.py      # Data Generator (Mock Revenue & Seasonality)
├── requirements.txt    # Project Dependencies
└── README.md           # Documentation

⚙️ Setup & Installation
1. Clone or Create the Repository
Bash
mkdir prediction_agent
cd prediction_agent

2. Set Up Virtual Environment
It is recommended to use a virtual environment to manage dependencies.

Bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

3. Install Dependencies
Create a requirements.txt file (or run the command below directly):

Bash
pip install openai langchain pandas matplotlib streamlit

4. Configure API Keys
You need an OpenAI API key to run the analysis.

Option A (Environment Variable):

Bash
export OPENAI_API_KEY="sk-proj-..."
Option B (.env file):
Create a .env file and add: OPENAI_API_KEY=sk-proj-... (requires python-dotenv).

5. Run the Application
Bash
streamlit run app.py