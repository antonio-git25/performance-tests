from fastapi import FastAPI, APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr, RootModel
import uvicorn
import random

app = FastAPI()

# Создаём роутер с общим префиксом и тегом для Swagger
courses_router = APIRouter(
    prefix="/api/v1/courses",  # Добавляет /api/v1/users ко всем путям в этом роутере
    tags=["courses-service"]  # Группирует маршруты под тегом "users-service" в документации
)


class CourseIn(BaseModel):
    title: str
    max_score: int
    min_score: int
    description: str


class CourseOut(CourseIn):
    id: int


class CoursesStore(RootModel):
    """In-memory хранилище пользователей вместо реальной БД"""
    root: list[CourseOut]  # Список всех пользователей

    def find_course(self, course_id: int) -> CourseOut | None:
        return next(filter(lambda course: course.id == course_id, self.root), None)

    def create_course(self, course_in: CourseIn) -> CourseOut:
        course = CourseOut(id=random.randint(125, 758), **course_in.model_dump())
        self.root.append(course)
        return course

    def update_course(self, course_id: int, course_in: CourseIn) -> CourseOut:
        index = next(index for index, course in enumerate(self.root) if course.id == course_id)
        # Создаём новый объект с тем же ID и обновлёнными полями
        updated = CourseOut(id=course_id, **course_in.model_dump())
        # Заменяем в списке
        self.root[index] = updated
        return updated

    def delete_course(self, course_id: int) -> None:
        self.root = [course for course in self.root if course.id != course_id]


# Инициализируем хранилище пустым списком
store = CoursesStore(root=[])


@courses_router.get("/{course_id}", response_model=CourseOut)
async def get_course(course_id: int):
    if not (course := store.find_course(course_id)):
        raise HTTPException(
            detail=f"Course with id {course_id} not found",
            status_code=status.HTTP_404_NOT_FOUND
        )

    return course


@courses_router.get("", response_model=list[CourseOut])
async def get_courses():
    return store.root


@courses_router.post("", response_model=CourseOut, status_code=status.HTTP_201_CREATED)
async def create_course(course: CourseIn):
    return store.create_course(course)


@courses_router.put("/{course_id}", response_model=CourseOut)
async def update_course(course_id: int, course: CourseIn):
    if not store.find_course(course_id):
        raise HTTPException(
            detail=f"Course with id {course_id} not found",
            status_code=status.HTTP_404_NOT_FOUND
        )
    return store.update_course(course_id, course)


@courses_router.delete("/{course_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_course(course_id: int):
    if not store.find_course(course_id):
        raise HTTPException(
            detail=f"Course with id {course_id} not found",
            status_code=status.HTTP_404_NOT_FOUND
        )

    store.delete_course(course_id)


# Подключаем роутер к основному приложению
app.include_router(courses_router)


if __name__ == "__main__":
    uvicorn.run(
        "fastapi_crud_course:app",
        host="127.0.0.1",
        port=8010,
        reload=True,
        log_level="info"
    )