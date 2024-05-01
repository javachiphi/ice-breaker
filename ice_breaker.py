from langchain.prompts.prompt import PromptTemplate
from langchain_openai import OpenAI
from third_parties.linkedin import scrape_linkedin_profile
from third_parties.twitter import scrape_user_tweet
from agents.twitter_lookup_agent import lookup as twitter_lookup_agent
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

from output_parsers import summary_parser, Summary
from typing import Tuple

def ice_break_with(name:str) -> str:
    linkedin_username = linkedin_lookup_agent(name=name)
    twitter_username = twitter_lookup_agent(name=name)

    

    summary_template = """
        Given the information from linkedin {information} 
        and twitter {tweets} I want you to create:

        Please provide:
        1. A short summary
        2. Two interesting facts from tweets
        3. linkedin profile URL

        Use both information from twitter and Linkedin
        \n{format_instructions}
     """

    llm = OpenAI()

    promptTemplate = PromptTemplate.from_template(
         template=summary_template,
         partial_variables={
             "format_instructions": summary_parser.get_format_instructions()
         }
        )

   
    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url=linkedin_username
    )

    tweets = scrape_user_tweet(username=twitter_username, mock=True)

    chain = promptTemplate | llm | summary_parser

    result = chain.invoke({"information": linkedin_data, "tweets": tweets})
    print(result)

if __name__ == '__main__':

    print('Ice Breaker enter')
    ice_break_with(name="Eden Marco Udemy")