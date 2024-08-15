from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from datetime import datetime
from typing import Dict

app = APIRouter()

# Modelo para a requisição
class Requisicao(BaseModel):
    id: int
    aluno_id: int
    descricao: str
    status: str = "Aberta"
    data_hora: str

# Banco de dados simulado
requisicoes: Dict[int, Requisicao] = {}

# Rota para criar uma nova requisição
@app.post("/", response_model=Requisicao, status_code=201)
async def create_requisicao(request: Request):
    data = await request.json()
    requisicao_id = len(requisicoes) + 1
    nova_requisicao = Requisicao(
        id=requisicao_id,
        aluno_id=data['aluno_id'],
        descricao=data['descricao'],
        data_hora=datetime.now().isoformat()
    )
    requisicoes[requisicao_id] = nova_requisicao
    return nova_requisicao

# Rota para atualizar o status de uma requisição existente
@app.put("/{id}", response_model=Requisicao)
async def update_requisicao(id: int, request: Request):
    if id in requisicoes:
        requisicoes[id].status = await request.json().get('status', requisicoes[id].status)
        return requisicoes[id]
    raise HTTPException(status_code=404, detail="Requisição não encontrada")
