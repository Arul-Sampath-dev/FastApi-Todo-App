from fastapi import Depends, FastAPI

from database.db import get_db_cursor
from schemas import Todo, TodoCreate

app = FastAPI(title="Todo Application")
id = 1


@app.get("/get-todos")
async def get_todos(cur=Depends(get_db_cursor)):
    # return [todo for todo in todos if not todo.deleted]
    cur.execute("""
            SELECT * FROM todos WHERE deleted = FALSE
        """)

    return cur.fetchall()


@app.post("/create-todo")
async def create_todo(data: TodoCreate, cur=Depends(get_db_cursor)):
    global id, todos
    dict_data = data.model_dump()
    dict_data["id"] = id
    id = id + 1
    # todos.append(Todo(**dict_data))
    todo = Todo(**dict_data)

    sql = """
        INSERT INTO todos(id, title, description, is_completed, deleted) VALUES (%s, %s, %s, %s, %s)
    """

    values = (todo.id, todo.title, todo.description, todo.is_completed, todo.deleted)

    cur.execute(sql, values)

    return {"message": "Todo Created Successfully", "status": 200, "Todo": todo}


@app.patch("/update-complete")
async def upate_complete(id: int, cur=Depends(get_db_cursor)):
    sql = """
        UPDATE todos
        SET is_completed = TRUE
        WHERE id = %s
    """

    cur.execute(sql, (id,))

    return {"message": "Success"}


@app.delete("/delete-todo")
async def delete_todo(id: int, cur=Depends(get_db_cursor)):
    sql = """
        UPDATE todos
        SET deleted = TRUE
        WHERE id = %s
    """

    cur.execute(sql, (id,))

    return {"message": "Deleted successfuly"}
