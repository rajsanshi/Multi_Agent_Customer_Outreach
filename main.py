import warnings
from crewai import Agent, Task, Crew,LLM
import os
from dotenv import load_dotenv
from Agents import sales_rep_agent,lead_sales_rep_agent
from Tasks import lead_profiling_task,personalized_outreach_task

load_dotenv

serper_api_key = os.getenv('SERPER_API_KEY')



llm = LLM(
    model="groq/llama-3.2-90b-text-preview",
    temperature=0.7
)

crew = Crew(
    agents=[sales_rep_agent, 
            lead_sales_rep_agent],
    
    tasks=[lead_profiling_task, 
           personalized_outreach_task],
	
    verbose=2,
	memory=True
)

inputs = {
    "lead_name": "OpenLearningHub",
    "industry": "Online Education",
    "key_decision_maker": "Sundar Pichai",
    "position": "Chief Innovation Officer",
    "milestone": "new AI-driven course platform launch"
}

result = crew.kickoff(inputs=inputs)


