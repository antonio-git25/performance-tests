from fastapi import FastAPI, Query, Path, Body  # Body — для аннотации тела запроса
from pydantic import BaseModel                  # BaseModel — базовый класс для моделей

app = FastAPI(title="basics")


# Pydantic-модель для описания структуры пользователя
class User(BaseModel):
    username: str
    email: str
    age: int

class UserResponse(BaseModel):
    username: str
    email: str
    age: int
    message: str


# GET-эндпоинт с query- и path-параметрами
@app.get("/api/v1/basics/{item_id}")
async def get_basics(
    name: str = Query("Alise", description="Имя пользователя"),
    item_id: int = Path(..., description="Идентификатор элемента")
):
    return {
        "message": f"Hello, {name}!",
        "description": f"Item number {item_id}"
    }


# POST-эндпоинт для создания пользователя
@app.post("/api/v1/basics/users", response_model=UserResponse)
async def create_user(
    user: User = Body(..., description="Данные нового пользователя")
) -> UserResponse:
    return UserResponse(
        username = user.username,
        email = user.email,
        age = user.age,
        message = "User created successfully!"
    )
