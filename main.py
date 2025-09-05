from fastapi import FastAPI
from pydantic import BaseModel

# CORRIGIDO: Nome da classe com 'T' maiúsculo
class Tarefa(BaseModel):
    id: int
    titulo: str
    descricao: str | None = None
    concluida: bool = False

app = FastAPI()

# Banco de dados em memória (uma lista simples)
db_tarefas = []

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Rota para LISTAR todas as tarefas
@app.get("/tarefas")
def listar_tarefas():
    return db_tarefas

# Rota para CRIAR uma nova tarefa
@app.post("/tarefas")
def criar_tarefa(tarefa: Tarefa):
    db_tarefas.append(tarefa.dict())
    return {"status": "Tarefa criada com sucesso!", "tarefa": tarefa}