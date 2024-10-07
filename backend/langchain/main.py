from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import OpenAI

load_dotenv()

question = "What is LangChain?"

if __name__ == "__main__":

    Summart_template = "give me information about {question}"

    template = PromptTemplate(input_variables=["question"], template=Summart_template)

    llm = OpenAI(temperature=0)

    chain = template | llm

    res = chain.invoke(input = {"question":question})

    print(res)