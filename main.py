import os
from constants import openai_key
from langchain.llms import OpenAI
import streamlit as st
import spacy
from langchain import PromptTemplate
from langchain.chains import LLMChain

from langchain.chains import SimpleSequentialChain

os.environ["OPENAI_API_KEY"] = openai_key
# nlp = spacy.load("en_core_web_sm")

st.title("XYZ")
input_text = st.text_input("search")

first_input = PromptTemplate(
    input_variables = ['name'],
    template = "Tell me about celebrity {name}"
)

llm = OpenAI(temperature=0.8)
chain = LLMChain(llm=llm, prompt=first_input, verbose=True)

# second_input = PromptTemplate(
#     input_variables = ['person'],
#     template  = "what is the dob of {person}"
# )

# chain = LLMChain(llm=llm, prompt=second_input, verbose=True, output_key="dob")


if input_text:  
    st.write(chain.run(input_text))