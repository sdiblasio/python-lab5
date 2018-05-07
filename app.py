from flask import Flask, render_template, request, redirect,url_for
import userdb

app = Flask(__name__)


@app.route('/')
def hello_world():
    return redirect(url_for('index'))

@app.route('/index')
def index():
    task_list = userdb.task_list()
    maxlength = 0
    for task in task_list:
        if not task['todo']:
            print("Empty object")
        if len(task['todo']) > maxlength:
            maxlength = len(task['todo'])
    if maxlength > 0:
        maxlength += 20
    return render_template("index.html", task_list=task_list, row_length=maxlength)


@app.route('/insert_page', methods=['POST'])
def insert_page():
    new_task = request.form['task']
    if request.form['urgent'] == "true":
        urgent = True
    else:
        urgent = False
    userdb.insert_task(new_task, urgent)
    return redirect(url_for('index'))


@app.route('/delete_page/<id_task>')
def delete_page(id_task):
    userdb.delete_task(id_task)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
