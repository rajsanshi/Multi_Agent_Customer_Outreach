import warnings
from crewai import Agent, Task, Crew,LLM
import os

llm = LLM(
    model="groq/llama-3.2-90b-text-preview",
    temperature=0.7
)

