from fanic import route, app
from sanic.response import json
from lazy.effect import lazy
from lazy.ef_app import EfApp


def main_handler(request):
    return (request &
            (lambda x: x.url) &
            (lambda x: json({"URL": x})))


@lazy
def EffectApp():
    route('/', main_handler)
    app.run(host="0.0.0.0", port=8000)
    return


EfApp(EffectApp)
