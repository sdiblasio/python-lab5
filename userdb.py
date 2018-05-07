import sqlite3
db_name = 'tasks.db'


def insert_task(task="example_task", urgent=True):
    sql = "INSERT INTO task(todo, urgent) VALUES(?,?)"
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute(sql, (task,urgent))
    cur.close()
    conn.commit()
    conn.close()
    return


def delete_task(id=0):
    sql = "DELETE FROM task WHERE id=?"
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute(sql, (id,))
    cur.close()
    conn.commit()
    conn.close()
    return


def task_list():
    sql = "SELECT * FROM task ORDER BY todo ASC"
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute(sql)
    todo_list = cur.fetchall()
    cur.close()
    conn.close()

    task_list = list()
    for task in todo_list:
        dict_task = dict()
        dict_task["id"] = task[0]
        dict_task["todo"] = task[1]
        task_list.append(dict_task)

    return task_list


if __name__ == '__main__':
    insert_task("Write Richard for the presentation")
    insert_task("Bring the mobile phone with you")
    delete_task(7)