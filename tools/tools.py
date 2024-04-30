from langchain_community.tools.tavily_search import TavilySearchResults

def get_profile_url_tavily(name: str):
  """
  Get the LinkedIn profile URL of a person using the Tavily search engine
  """
  search = TavilySearchResults()
  res = search.run(f"{name}")
  return res[0]["url"]
 