from langchain_community.chat_models import ChatOllama

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

llm = ChatOllama(model="llama3", temperature=0.7)


def generate_restaurant_name_and_items(cuisine):
    # Chain 1: Restaurant Name
    prompt_template_name = PromptTemplate(
        input_variables=["cuisine"],
        template="I want to open a restaurant for {cuisine} food. Suggest only one fancy name for this. "
        "Do not give any description.",
    )

    name_chain = LLMChain(
        llm=llm, prompt=prompt_template_name, output_key="restaurant_name"
    )

    # Chain 2: Menu Items
    prompt_template_items = PromptTemplate(
        input_variables=["restaurant_name"],
        template="""Suggest some menu items for {restaurant_name}. Only return it as a comma separated string. 
        Do not add any kind of description.""",
    )

    food_items_chain = LLMChain(
        llm=llm, prompt=prompt_template_items, output_key="menu_items"
    )

    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=["cuisine"],
        output_variables=["restaurant_name", "menu_items"],
    )

    response = chain({"cuisine": cuisine})
    response["restaurant_name"] = response["restaurant_name"].replace('"', "")
    return response


if __name__ == "__main__":
    print(generate_restaurant_name_and_items("Indian"))
