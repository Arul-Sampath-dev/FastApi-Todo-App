from pydantic import BaseModel


class Todo(BaseModel):
    id: int
    title: str
    description: str
    is_completed: bool | None = False
    deleted: bool | None = False


class TodoCreate(BaseModel):
    title: str
    description: str
