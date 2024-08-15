from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from typing import Dict

app = APIRouter()

# Modelo para o curso
class Curso(BaseModel):
    id: int
    nome: str
    descricao: str

# Banco de dados simulado
cursos: Dict[int, Curso] = {}

# Rota para listar todos os cursos
@app.get("/", response_model=Dict[int, Curso])
def list_cursos():
    return cursos

# Rota para obter um curso pelo ID
@app.get("/{id}", response_model=Curso)
def get_curso(id: int):
    curso = cursos.get(id)
    if curso:
        return curso
    raise HTTPException(status_code=404, detail="Curso não encontrado")

# Rota para criar um novo curso
@app.post("/", response_model=Curso, status_code=201)
async def create_curso(request: Request):
    data = await request.json()
    curso_id = len(cursos) + 1
    novo_curso = Curso(id=curso_id, **data)
    cursos[curso_id] = novo_curso
    return novo_curso

# Rota para atualizar um curso existente
@app.put("/{id}", response_model=Curso)
async def update_curso(id: int, request: Request):
    if id in cursos:
        cursos[id] = cursos[id].copy(update=await request.json())
        return cursos[id]
    raise HTTPException(status_code=404, detail="Curso não encontrado")
