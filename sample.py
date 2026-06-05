from fastapi import Depends, FastAPI
from pydantic import BaseModel

from database.db import get_db_cursor


class Todo(BaseModel):
    id: int
    title: str
    description: str
    is_completed: bool | None = False
    deleted: bool | None = False


class TodoCreate(BaseModel):
    title: str
    description: str


# class TodoUpdate(BaseModel):
#     id: int
#     is_completed: bool = True


app = FastAPI(title="Todo Application")


id = 1
todos: list[Todo] = []


@app.get("/")
async def index(cur=Depends(get_db_cursor)):
    # cur.execute("""
    #         CREATE TABLE IF NOT EXISTS todos(
    #             id INT PRIMARY KEY,
    #             title VARCHAR(255),
    #             description VARCHAR(255),
    #             is_completed BOOLEAN,
    #             deleted BOOLEAN
    #         )
    #     """)

    return {"message": "Hello World"}


@app.post("/create-todo")
async def create_todo(data: TodoCreate):
    global id, todos
    dict_data = data.model_dump()
    dict_data["id"] = id
    id = id + 1
    todos.append(Todo(**dict_data))
    return {"message": "Todo Created Successfully", "status": 200}


@app.get("/get-todos")
async def get_todos():
    return [todo for todo in todos if not todo.deleted]


# @app.put("/update-todo")
# async def update_todos(update_data: TodoUpdate):
#     for todo in todos:
#         if todo.id == update_data.id:
#             update_dict = update_data.model_dump()

#             for key, value in update_dict.items():
#                 # print(key, value)
#                 setattr(todo, key, value)

#             return {"message": "Updated"}

#     return {"message": "Invalid ID"}


@app.patch("/update-complete")
async def upate_complete(id: int):
    for todo in todos:
        if todo.id == id:
            todo.is_completed = True
            return {"message": "completed"}

    return {"message": "failed"}


@app.patch("/delete-todo")
async def delete_todo(id: int):
    for todo in todos:
        if todo.id == id:
            todo.deleted = True
            return {"message": "Deleted"}

    return {"message": "Deletion failed"}
