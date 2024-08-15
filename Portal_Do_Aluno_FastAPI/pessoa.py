from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from typing import Dict

app = APIRouter()

# Modelo para a pessoa
class Pessoa(BaseModel):
    id: int
    nome: str
    idade: int
    email: str

# Banco de dados simulado
pessoas: Dict[int, Pessoa] = {}

# Rota para listar todas as pessoas
@app.get("/", response_model=Dict[int, Pessoa])
def list_pessoas():
    return pessoas

# Rota para obter uma pessoa pelo ID
@app.get("/{id}", response_model=Pessoa)
def get_pessoa(id: int):
    pessoa = pessoas.get(id)
    if pessoa:
        return pessoa
    raise HTTPException(status_code=404, detail="Pessoa não encontrada")

# Rota para criar uma nova pessoa
@app.post("/", response_model=Pessoa, status_code=201)
async def create_pessoa(request: Request):
    data = await request.json()
    pessoa_id = len(pessoas) + 1
    nova_pessoa = Pessoa(id=pessoa_id, **data)
    pessoas[pessoa_id] = nova_pessoa
    return nova_pessoa

# Rota para atualizar uma pessoa existente
@app.put("/{id}", response_model=Pessoa)
async def update_pessoa(id: int, request: Request):
    if id in pessoas:
        pessoas[id] = pessoas[id].copy(update=await request.json())
        return pessoas[id]
    raise HTTPException(status_code=404, detail="Pessoa não encontrada")
