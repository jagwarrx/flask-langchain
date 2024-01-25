from flask import Flask
from llama_index.program import OpenAIPydanticProgram
from llama_index.llms import OpenAI
from pydantic import BaseModel
from typing import List


app = Flask(__name__)

class WorkExperience(BaseModel):
    """Data model for a song."""
    date: str
    place: str
    projects: str

class Education(BaseModel):
    """Data model for a song."""
    date: str
    place: str


class Resume(BaseModel):
    """Data model for an album."""

    name: str
    email: str
    skills: str
    experience: List[WorkExperience]
    education: List[Education]

program = OpenAIPydanticProgram.from_defaults(
    output_cls=Resume,
    llm=OpenAI(temperature=0, model="gpt-4-0613", api_key="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"),
    prompt_template_str=(
        "Please extract the following spanish resume text into a structured data:"
        " {input_str}. The column names are the following: ['Name', 'Email',"
        " 'Skills', 'Experience']. Do not specify additional parameters that"
        " are not in the function schema. "
    ),
    verbose=True,
)

text2 = """
EXPERIENCIA
2021 - 2023 Seven Electronics
Vendedor al público y encargado de
local de accesorios de celulares y tecnología en general. Control de cajas y de gastos del local.
2018 - 2019 IMALEX, CA
Agente de ventas de insumos médicos. Encargado de atención directa al cliente para dar información sobre productos y precios.
2017 Internatiocall, inc
Agente de ventas por teléfono. Encargado de llamar a posibles compradores y concertar citas para instalaciones de paneles solares.
Juan Guevara
Juan Domingo Perón, 1671 Ciudad Autónoma de Buenos Aires
juanjo278@gmail.com
(+54) 11 2253 9508
26 años
FORMACIÓN ACADÉMICA
Bachiller en Ciencias, Colegio Ramón Pierluissi Valencia, Venezuela
CURSOS
Curso de Técnicas básicas e intermedias para Baristas - 2017 M&Y Baristas Training, Valencia, Venezuela.
Curso de Oratoria - 2014 Instituto Ciencicrea, Valencia, Venezuela
HABILIDADES
Manejo de Microsoft Office
Rápido aprendizaje
Atención al detalle
Redacción buena, rápida y fluida
IDIOMAS
Español - Nativo
Inglés - Fluido
"""

@app.get('/')
def hello_world():
    output = program(input_str=text2)
    print("Hello")
    print(output)
  
