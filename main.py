import warnings
from crewai import Agent, Task, Crew,LLM
import os
from dotenv import load_dotenv

load_dotenv

serper_api_key = os.getenv('SERPER_API_KEY')



llm = LLM(
    model="groq/llama-3.2-90b-text-preview",
    temperature=0.7
)

