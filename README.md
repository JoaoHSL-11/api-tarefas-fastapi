# 🚀 Task Management API

A REST API for task management (To-Do list) built with Python and FastAPI as part of my learning journey and back-end development portfolio.

## ✨ Main Features

-   **Create tasks:** Add new tasks to your list.
-   **List tasks:** View all registered tasks.
-   (Coming soon) Update tasks.
-   (Coming soon) Delete tasks.

## 🛠️ Technologies Used

-   **Language:** Python 3.10+
-   **Framework:** FastAPI
-   **Server:** Uvicorn
-   **Data Validation:** Pydantic

## ▶️ How to Run the Project

Follow the steps below to run the project locally.

### Prerequisites

-   Python 3.10 or higher
-   Git

### Installation

1.  Clone the repository:
    ```bash
    git clone [https://github.com/JoaoHSL-11/api-tarefas-fastapi.git](https://github.com/JoaoHSL-11/api-tarefas-fastapi.git)
    ```
2.  Navigate to the project directory:
    ```bash
    cd api-tarefas-fastapi
    ```
3.  Create and activate a virtual environment:
    ```bash
    # Linux/macOS
    python3 -m venv venv
    source venv/bin/activate

    # Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```
4.  Install the dependencies:
    ```bash
    pip install fastapi "uvicorn[standard]"
    ```

### Running the Application

1.  With the virtual environment activated, start the server:
    ```bash
    uvicorn main:app --reload
    ```
2.  The API will be available at `http://12.0.0.1:8000`.
3.  Access
