from dotenv import load_dotenv
load_dotenv()

from agents import build_reader_agent , build_search_agent , critic_chain , writer_chain

def run_research_pipeline(topic : str) -> dict:
    
    #shared state dictionary
    state = {}
    
    #-------------step 1 search agent----------------------- 
    print("\n search agent is working")
    print("-"*100)
    
    search_agent = build_search_agent()
    
    search_result = search_agent.invoke(
        {
            "messages" : [("user" , f"find recent ,  reliable and detailed information about {topic}")]
        }
    )
    
    state['search_result'] = search_result['messages'][-1].text #get the last AI response from the result list
    
    print("\n search result =" , state['search_result']) 
    
    
    #----------step 2 scrapping ------------------------------
    print("\n scrapper agent is working")
    print("-"*100)
    
    reader_agent = build_reader_agent()
    reader_result = reader_agent.invoke(
        {
            "messages" : [("user" , 
                          f"Based on the following search results  about {topic}"
                          f"pick the most relevant URL and scrape it for deeper content. \n \n"
                          f"Search Result : {state['search_result'][:800]}")]
        }
    )
    
    state['scrapped_result'] = reader_result['messages'][-1].text
    
    print("\n scarped content" , state["scrapped_result"])
    
    #---------------step 3 writer chain-------------------------
    print("\n drafting the result")
    print("-"*100)    
    
    combined_research = ( #result from both (search result and scraped result)
        f"SEARCH RESULT : {state['search_result']}\n"
        f"SCRAPED RESULT : {state['scrapped_result']}"
    )
    report = writer_chain.invoke(
        {
            'Topic' : topic,
            'Research' : combined_research            
        }
    )
    
    state['report'] = report
    
    print("\n final report : \n" , state["report"])
    
    #---------------step 4 critic chain--------------------------------
    
    print("\n critic agent is working")
    print("-"*100)
    
    critic_report = critic_chain.invoke(
        {
            'report' : report
        }
    )
    
    state['critic_report'] = critic_report
    
    print("\n critic report : \n" , state['critic_report'])
    
    return state 



if __name__ == "__main__":
    topic = input("Enter the Topic :  ")
    run_research_pipeline(topic)