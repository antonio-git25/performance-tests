from fastapi import FastAPI, Query, Path, Body, APIRouter, HTTPException, status, Depends
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="basics")

router = APIRouter(
    prefix="/api/v1",
    tags=["Basics"]
)

# Pydantic-модель для описания структуры пользователя
class User(BaseModel):
    username: str
    email: str
    age: int

class UserResponse(BaseModel):
    username: str
    email: str
    message: str


# Зависимость: проверка минимального возраста
def validate_min_age(min_age: int = 18):
    def checker(user: User):
        if user.age < min_age:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"User must be at6 least {min_age} years old"
            )
        return user
    return checker


# GET-эндпоинт с query- и path-параметрами
@router.get("/basics")
async def get_basics(
    name: str = Query("Alise", description="Имя пользователя"),
    #item_id: int = Path(..., description="Идентификатор элемента")
):
    return {
        "message": f"Hello, {name}!"
        #"description": f"Item number {item_id}"
    }


# POST-эндпоинт для создания пользователя
@router.post("/basics/users", response_model=UserResponse)
async def create_user(
    user: User = Body(..., description="Данные нового пользователя")
) -> UserResponse:
    return UserResponse(
        username = user.username,
        email = user.email,
        message = "User created successfully!"
    )


@router.post("/basics/register", summary="Регистрация нового пользователя")
async def register_user(user: User = Depends(validate_min_age(min_age=21))):
    return {
        "message:": f"User {user.username} registered successfully",
        "email": user.email,
        "age": user.age
    }


app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(
        "fastapi_basics:app",
        host="127.0.0.1",
        port=8010,
        reload=True,
        log_level="info"
    )