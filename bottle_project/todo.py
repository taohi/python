#!/usr/bin/python
import sqlite3
from bottle import route,run,debug,template,request

@route('/todo')
def todo_list():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id,task FROM todo WHERE status LIKE '1'")
    result = c.fetchall()
    c.close()
    #return str(result)
    output = template('make_table',rows = result)
    return output

@route('/new',method="GET")
def new_item():
    if request.GET.get('save','').strip():
        new = request.GET.get('task','').strip()
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("INSERT INTO todo (task,status) VALUES(?,?)",(new,1))
        new_id = c.lastrowid
        conn.commit()
        c.close()
        return '<p>New task Already Added.ID:%s</p>'%new_id
    else:
        return template('new_task.tpl') 

@route('/edit/:no',method='GET')
def edit_item(no):
    if request.GET.get('save','').strip():
        edit = request.GET.get('task','').strip()
        status=request.GET.get('status','').strip()

        if status == 'open':
            status=1
        else:
            status = 0
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("UPDATE todo SET task=?,status=?WHERE id LIKE ?",(edit,status,no))
        conn.commit()
        c.close()
        return '<p>Item with ID:%s was succesfully updated.</p>'%no
    else:
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("SELECT task FROM todo WHERE id LIKE ?",str(no))
        cur_data = c.fetchone()
        return template('edit_task',old = cur_data,no = no)

debug(True)
#run(port = 8000,host = '115.156.166.180')
run(reloader = True,port = 8000,host ='127.0.0.1') 
