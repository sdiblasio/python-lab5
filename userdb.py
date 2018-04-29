import sqlite3
db_name = 'tasks.db'


def insert_task(task="example_task"):
    sql = "INSERT INTO task(todo) VALUES(?)"
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute(sql, (task,))
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
    sql = "SELECT ? FROM task"
    conn = sqlite3.connect(db_name)
    elem = "todo"
    cur = conn.cursor()
    cur.execute(sql, (elem,))
    todo_list = cur.fetchall()
    '''if not todo_list:
        print("No todos")'''
    cur.close()
    elem = "id"
    cur = conn.cursor()
    cur.execute(sql, (elem,))
    ids = cur.fetchall()
    '''if not ids:
        print("No ids")'''
    cur.close()
    conn.close()
    tasks_list = dict()
    for (id, todo) in (ids, todo_list):
        tasks_list[id] = todo
    return (ids, tasks_list)


if __name__ == '__main__':
    insert_task("Write Richard for the presentation")
    insert_task("Bring the mobile phone with you")
    delete_task(7)