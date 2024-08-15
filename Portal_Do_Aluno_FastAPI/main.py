from fastapi import FastAPI
from pessoa import pessoa_router
from curso import curso_router
from aluno import aluno_router
from requisicao import requisicao_router

app = FastAPI()

# Register Routers
app.include_router(pessoa_router, prefix="/pessoa")
app.include_router(curso_router, prefix="/curso")
app.include_router(aluno_router, prefix="/aluno")
app.include_router(requisicao_router, prefix="/requisicao")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)
