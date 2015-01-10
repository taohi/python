#!/usr/bin/python
import sqlite3
from bottle import route,run,debug,template

@route('/todo')
def todo_list():
    #return template('index')
    return template('make_table')
    #return "loworld"
@route('/new')
def new_item():
    return "hello new item"
debug(True)
#run(port = 8000,host = '115.156.166.180')
run(reloader = True,port = 8000,host = localhost) 
