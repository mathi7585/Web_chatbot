from tavily import TavilyClient
import os
from dotenv import load_dotenv
load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def web_search(query):
    response = client.search(
        query=query,
        search_depth="advanced",
        max_results=5
    )

    results = []
    for r in response["results"]:
        results.append(r["content"])

    return "\n".join(results)
