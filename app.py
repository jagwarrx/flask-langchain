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
    console.log("hello world"
    return "hello world"
