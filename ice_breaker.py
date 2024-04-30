from langchain.prompts.prompt import PromptTemplate
from langchain_openai import OpenAI
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup


def ice_break_with(name:str) -> str:
    linkedin_username = lookup(name=name)

    summary_template = """
        Given the information: {information}

        Please provide:
        1. A short summary of the information.
        2. Two interesting facts derived from the information.
     """

    model = OpenAI()

    promptTemplate = PromptTemplate.from_template(summary_template)

    chain = promptTemplate.pipe(model)
    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url=linkedin_username
    )

    result = chain.invoke({"information": linkedin_data})
    print(result)

if __name__ == '__main__':

    print('Ice Breaker enter')
    ice_break_with(name="Eden Marco Udemy")