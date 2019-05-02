from fanic import route, app
from sanic.response import html
from lazy.effect import lazy, pure
from lazy.ef_app import EfApp
from lazy.resource import Resource

import sqlite3

conn = sqlite3.connect('example.db')
transactor = Resource.make(lazy(lambda: conn.cursor())())(db_close)

INIT_DB_QUARY = 'CREATE TABLE users(age text, name text)'
INSERT_LAS_DB_QUARY = 'INSERT INTO users VALUES("19", "Las aka Wonho")'


@lazy
def db_close(cusor):
    cusor.commit()
    cusor.close()


def main_handler(request):
    transactor.use(lambda x: [x.execute('SELECT name FROM users'), x]).map(
        lambda x: x[1].fetchone()).map(lambda x: print(x)).execute()
    return (request &
            (lambda x: "This Page Made By Fanic(Sanic Functional Wrapper)") &
            (lambda x: "<h1>" + x + "</h1>") &
            (lambda x: html(x)))


def hello(request, name):
    return (name &
            (lambda x: "Hello " + x + "~!") &
            (lambda x: "<h1>" + x + "</h1>") &
            (lambda x: html(x)))


@lazy
def EffectApp():
    route('/', main_handler)
    route('hello/<name>', hello)
    transactor.use(lambda x: [x.execute(INIT_DB_QUARY), x]).map(
        lambda x: x[1].execute(INSERT_LAS_DB_QUARY)).execute()
    app.run(host="0.0.0.0", port=8000)
    return


EfApp(EffectApp)
