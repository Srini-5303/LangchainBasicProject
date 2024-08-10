import os

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain
from langchain.chains import LLMChain

os.environ['OPENAI_API_KEY'] = "OPEN_API_KEY"

llm = OpenAI(model="gpt-3.5-turbo-instruct",temperature=0.8)

# from langchain.llms import HuggingFaceHub
#
# hf = HuggingFaceHub(repo_id="gpt2", huggingfacehub_api_token="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")


def generate_rest_name_and_menu(cuisine):
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this"
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest some menu items for {restaurant_name}. Return it as a comma separated values"
    )

    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'menu_items']
    )

    response = chain({'cuisine': cuisine})

    return response
