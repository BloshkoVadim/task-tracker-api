from fastapi import FastAPI

# Создаём экземпляр приложения FastAPI
app = FastAPI(
    tittle="Task Tracker API",
    description="API для управления персольнальными задачами",
    version="0.1.0"
)

# Тестовый эндпоинт
@app.get("/")
def read_root():
    return {"message": "Добро пожаловать в Task Tracker API!"}


# /about endpoint
@app.get("/about")
def get_about():
    return {
        "name": "John",
        "goal": "To become president"}
