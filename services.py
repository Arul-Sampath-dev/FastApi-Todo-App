from schemas import Todo


class TodoHandler:
    id = 2

    @classmethod
    def get_all_todos(cls, cur):
        cur.execute("""
                SELECT * FROM todos WHERE deleted = FALSE
        """)
        return cur.fetchall()

    @classmethod
    def create_a_todo(cls, cur, data):
        # global id
        dict_data = data.model_dump()
        dict_data["id"] = cls.id
        cls.id = cls.id + 1
        # todos.append(Todo(**dict_data))
        todo = Todo(**dict_data)

        sql = """
            INSERT INTO todos(id, title, description, is_completed, deleted) VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            todo.id,
            todo.title,
            todo.description,
            todo.is_completed,
            todo.deleted,
        )

        cur.execute(sql, values)

        return todo

    @classmethod
    def update_changes(cls, cur, id):

        sql = """
            UPDATE todos
            SET is_completed  = TRUE
            WHERE id = %s
        """

        cur.execute(sql, (id,))

        return {"message": "Success"}

    @classmethod
    def delete_todo(cls, cur, id):

        sql = """
            UPDATE todos
            SET deleted  = TRUE
            WHERE id = %s
        """

        cur.execute(sql, (id,))

        return {"message": "Success"}
