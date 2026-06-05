from fastapi import Depends, FastAPI

from database.db import get_db_cursor
from schemas import TodoCreate
from services import TodoHandler

app = FastAPI(title="Todo Application")
id = 1


@app.get("/get-todos")
async def get_todos(cur=Depends(get_db_cursor)):
    return TodoHandler.get_all_todos(cur)


@app.post("/create-todo")
async def create_todo(data: TodoCreate, cur=Depends(get_db_cursor)):
    return {"message": "Sucess", "todo": TodoHandler.create_a_todo(cur, data)}


@app.patch("/{id}/update-complete/")
async def upate_complete(id: int, cur=Depends(get_db_cursor)):
    return TodoHandler.update_changes(cur, id)


@app.delete("/{id}/delete-todo")
async def delete_todo(id: int, cur=Depends(get_db_cursor)):
    return TodoHandler.delete_todo(cur, id)
    # sql = """
    #     UPDATE todos
    #     SET deleted = TRUE
    #     WHERE id = %s
    # """

    # cur.execute(sql, (id,))

    # return {"message": "Deleted successfuly"}
