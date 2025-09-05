# 🚀 API de Gerenciamento de Tarefas

API REST para gerenciamento de tarefas (To-Do list) construída com Python e FastAPI como parte do meu aprendizado e portfólio de desenvolvimento back-end.

## ✨ Funcionalidades Principais

-   **Criar tarefas:** Adicione novas tarefas à sua lista.
-   **Listar tarefas:** Visualize todas as tarefas cadastradas.
-   (Em breve) Atualizar tarefas.
-   (Em breve) Deletar tarefas.

## 🛠️ Tecnologias Utilizadas

-   **Linguagem:** Python 3.10+
-   **Framework:** FastAPI
-   **Servidor:** Uvicorn
-   **Validação de Dados:** Pydantic

## ▶️ Como Executar o Projeto

Siga os passos abaixo para executar o projeto localmente.

### Pré-requisitos

-   Python 3.10 ou superior
-   Git

### Instalação

1.  Clone o repositório:
    ```bash
    git clone [https://github.com/JoaoHSL-11/api-tarefas-fastapi.git](https://github.com/JoaoHSL-11/api-tarefas-fastapi.git)
    ```
2.  Navegue até o diretório do projeto:
    ```bash
    cd api-tarefas-fastapi
    ```
3.  Crie e ative um ambiente virtual:
    ```bash
    # Linux/macOS
    python3 -m venv venv
    source venv/bin/activate

    # Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```
4.  Instale as dependências:
    ```bash
    pip install fastapi "uvicorn[standard]"
    ```

### Rodando a Aplicação

1.  Com o ambiente virtual ativado, inicie o servidor:
    ```bash
    uvicorn main:app --reload
    ```
2.  A API estará disponível em `http://127.0.0.1:8000`.
3.  Acesse a documentação interativa em `http://127.0.0.1:8000/docs`.

## 📝 Endpoints da API

| Método | Endpoint     | Descrição                  |
| ------ | ------------ | -------------------------- |
| `GET`  | `/tarefas`   | Lista todas as tarefas     |
| `POST` | `/tarefas`   | Cria uma nova tarefa       |
