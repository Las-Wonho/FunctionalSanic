from sanic import Sanic
from sanic.response import json
from lazy.effect import pure, lazy
from lazy.ef_app import EfApp

app = Sanic()


def route(url, f):
    async def F(*params):
        effect_params = [pure(i) for i in params]
        x = f(*effect_params).execute
        return x
    app.route(url)(F)


@lazy
def EffectApp():
    route('/', f)
    app.run(host="0.0.0.0", port=8000)
    return
