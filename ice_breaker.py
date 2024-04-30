from langchain.prompts.prompt import PromptTemplate
from langchain_openai import OpenAI
from third_parties.linkedin import scrape_linkedin_profile

if __name__ == '__main__':
    print('Hello, World!')

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
        linkedin_profile_url="https://www.linkedin.com/in/eden-marco/",
        mock=True,
    )

    result = chain.invoke({"information": linkedin_data})
    print(result)