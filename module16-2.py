from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
def root():
    return "Главная страница"


@app.get("/user/admin")
def admin():
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")
def user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='42')]):
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user/{username}/{age}")
def user_info(
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='30')]
):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"