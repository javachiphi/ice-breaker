from langchain.prompts.prompt import PromptTemplate
from langchain_openai import OpenAI

if __name__ == '__main__':
    print('Hello, World!')

    information = "Elon Reeve Musk (/ˈiːlɒn/ EE-lon; born June 28, 1971) is a businessman and investor. He is the founder, chairman, CEO, and CTO of SpaceX; angel investor, CEO, product architect, and former chairman of Tesla, Inc.; owner, executive chairman, and CTO of X Corp.; founder of the Boring Company and xAI; co-founder of Neuralink and OpenAI; and president of the Musk Foundation. He is one of the wealthiest people in the world; as of April 2024, Forbes estimates his net worth to be $178 billion."

    summary_template = """
    Given the information: {information}

    Please provide:
    1. A short summary of the information.
    2. Two interesting facts derived from the information.
    """

    model = OpenAI()

    promptTemplate = PromptTemplate.from_template(summary_template)

    chain = promptTemplate.pipe(model)

    result = chain.invoke({"information": information})
    print(result)