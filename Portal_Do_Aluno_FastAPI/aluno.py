from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from typing import Dict, List

app = APIRouter()

# Modelo para o aluno
class Aluno(BaseModel):
    id: int
    pessoa_id: int
    curso_id: int
    isAtivo: bool = True

# Banco de dados simulado
alunos: Dict[int, Aluno] = {}

# Rota para listar todos os alunos ativos
@app.get("/", response_model=List[Aluno])
def list_alunos():
    return [aluno for aluno in alunos.values() if aluno.isAtivo]

# Rota para associar um novo aluno
@app.post("/{id}", response_model=Aluno, status_code=201)
async def associate_aluno(id: int, request: Request):
    data = await request.json()
    aluno_id = len(alunos) + 1
    novo_aluno = Aluno(id=aluno_id, pessoa_id=id, curso_id=data['curso_id'])
    alunos[aluno_id] = novo_aluno
    return novo_aluno

# Rota para deletar um aluno (soft delete)
@app.delete("/{id}")
def delete_aluno(id: int):
    if id in alunos:
        alunos[id].isAtivo = False
        return {"message": "Aluno deletado virtualmente"}
    raise HTTPException(status_code=404, detail="Aluno não encontrado")
