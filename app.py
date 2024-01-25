from flask import Flask
from llama_index.program import (
    OpenAIPydanticProgram,
    DFFullProgram,
    DataFrame,
    DataFrameRowsOnly,
)
from llama_index.llms import OpenAI


app = Flask(__name__)

@app.get('/')
def hello_world():
    program = OpenAIPydanticProgram.from_defaults(
    llm=OpenAI(temperature=0, model="gpt-4-0613", api_key="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"),
    prompt_template_str=(
        "Please extract the following spanish resume text into a structured data:"
        " {input_str}. The column names are the following: ['Name', 'Email',"
        " 'Skills', 'Experience']. Do not specify additional parameters that"
        " are not in the function schema. "
    ),
    verbose=True,
)
    return "hello world"
