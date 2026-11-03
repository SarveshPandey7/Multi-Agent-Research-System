#core of the project
from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from tools import web_search_tool, web_scraper_tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#-------------------model setup-------------------------------------
llm = ChatGoogleGenerativeAI(model = "gemini-3.5-flash-lite")

#-------------------agents-------------------------------------------
#agent 1 (Search Agent)
def build_search_agent():
    return create_agent(
        model = llm ,
        tools = [web_search_tool]
    )
    

#agent 2 (Scrapper or Reader Agent)
def build_reader_agent():
    return create_agent(
        model = llm ,
        tools = [web_scraper_tool]
    )
    

#----------------------chains--------------------------------------
#writer chain

writer_prompt = ChatPromptTemplate.from_messages(
    [
        ("system" , "You are an expert Research writer. write Clean , structured and insightful reports."),
        ("human" , """Write a detailed Research report on the topic below
         Topic : {Topic}
         
         Research Gathered : {Research}
         
         Structure the Report as:
         - Introduction
         - Key findings (minimum 3 well explained Points)
         - Sonclusion
         - Sources (list all the URLs found in the research)
         
         
         Be detailed ,  factual and Professional""")
    ]
)

writer_chain = writer_prompt | llm | StrOutputParser()


#critic chain

critic_prompt = ChatPromptTemplate.from_messages(
    [
        ("system" , "You are a Sharp and constructive reseach critic. Be honest and Specific."),
        ("human" , """Review the research report below and evaluate it strictly.
         
         Report: {report}
         
         Respond in this  exact format:
         
         Score : x/10 
         
         Strengths:
         - .........
         - .........
         
         
         Areas to Improve:
         - ..........
         - ..........
         
         
         one line verdict:
         - ..........
         
         """)
    ]
)

critic_chain = critic_prompt | llm | StrOutputParser()