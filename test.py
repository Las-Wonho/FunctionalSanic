from fanic import route, app
from sanic.response import html
from lazy.effect import lazy
from lazy.ef_app import EfApp


def main_handler(request):
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
    app.run(host="0.0.0.0", port=8000)
    return


EfApp(EffectApp)
