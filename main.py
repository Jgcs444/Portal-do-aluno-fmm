#Importando a biblioteca FastAPI
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
from db import cursos, pessoas
#Instânciando a variável 'app' em uma função fastapi()

app = FastAPI()

# Modelos Pydantic para validação dos dados
class Curso(BaseModel):
    nome: str

class Pessoa(BaseModel):
    nome: str

# CRUD para Cursos
@app.get("/cursos/")
def read_cursos():
    return cursos

@app.get("/cursos/{curso_id}")
def read_curso(curso_id: int):
    curso = cursos.get(curso_id)
    if curso:
        return curso
    raise HTTPException(status_code=404, detail="Curso não encontrado")

@app.post("/cursos/")
def create_curso(curso: Curso):
    curso_id = max(cursos.keys()) + 1 if cursos else 1
    cursos[curso_id] = curso.dict()
    return cursos[curso_id]

@app.put("/cursos/{curso_id}")
def update_curso(curso_id: int, curso: Curso):
    if curso_id in cursos:
        cursos[curso_id] = curso.dict()
        return cursos[curso_id]
    raise HTTPException(status_code=404, detail="Curso não encontrado")

@app.delete("/cursos/{curso_id}")
def delete_curso(curso_id: int):
    if curso_id in cursos:
        return cursos.pop(curso_id)
    raise HTTPException(status_code=404, detail="Curso não encontrado")

# CRUD para Pessoas
@app.get("/pessoas/")
def read_pessoas():
    return pessoas

@app.get("/pessoas/{pessoa_id}")
def read_pessoa(pessoa_id: int):
    pessoa = pessoas.get(pessoa_id)
    if pessoa:
        return pessoa
    raise HTTPException(status_code=404, detail="Pessoa não encontrada")

@app.post("/pessoas/")
def create_pessoa(pessoa: Pessoa):
    pessoa_id = max(pessoas.keys()) + 1 if pessoas else 1
    pessoas[pessoa_id] = pessoa.dict()
    return pessoas[pessoa_id]

@app.put("/pessoas/{pessoa_id}")
def update_pessoa(pessoa_id: int, pessoa: Pessoa):
    if pessoa_id in pessoas:
        pessoas[pessoa_id] = pessoa.dict()
        return pessoas[pessoa_id]
    raise HTTPException(status_code=404, detail="Pessoa não encontrada")

@app.delete("/pessoas/{pessoa_id}")
def delete_pessoa(pessoa_id: int):
    if pessoa_id in pessoas:
        return pessoas.pop(pessoa_id)
    raise HTTPException(status_code=404, detail="Pessoa não encontrada")
