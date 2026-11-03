# we will create tools here
from dotenv import load_dotenv
load_dotenv()

from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os

from rich import print

tavily = TavilyClient(api_key = os.getenv("TAVILY_API_KEY"))

#----------tool1--------------
@tool
def web_search_tool(query : str) -> dict:
    """search the internet or web for the recent and reliable information
    about the given query/topic.
    Returns titles , urls and  snippets"""
    
    if tavily is None:
        return {"error" : "no tavily client found"}
    
    try:
        response = tavily.search(
            query = f"recent and reliable information about {query}",
            topic = "general",
            max_results = 5
        )
        
        information = []
        
        for result in response.get("results" , []):
            information.append({
                "title" : result.get("title"),
                "url" : result.get("url"),
                "snippet" : result.get("content")[:300]
            })
            
            
        return {
            "topic" : query,
            "information" : information
        }
            
    except Exception as e:
        return {"error" : f"search failed : {e}"}
    
    
#-------------tool2-----------------------
@tool
def web_scraper_tool(url : str) -> dict:
    """scrape the given url and return the text content of the page"""
    
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return {"error" : f"failed to fetch the url, status code : {response.status_code}"}
        
        # set a user-agent header to avoid being blocked by some websites / work as a real user
        resp = requests.get(url , headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"})  
        
        soup = BeautifulSoup(resp.content , "html.parser")
        # soup = BeautifulSoup(response.content , "html.parser")
        
         #remove unwanted tags like script, style, header, footer, nav from the html content
        for tag in ["script", "style", "header", "footer", "nav"]:
            for element in BeautifulSoup(response.content, "html.parser").find_all(tag):
                element.decompose()
        
        text_content = soup.get_text(separator="\n", strip=True)
        
        return {
            "url" : url,
            "text_content" : text_content[:3000]  # returning first 3000 characters
        }
        
    except Exception as e:
        return {"error" : f"scraping failed : {e}"}