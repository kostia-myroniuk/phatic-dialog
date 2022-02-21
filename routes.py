from sanic import Sanic
from sanic.response import json
from helper.main import resp


async def process_message(request):
    requst_object = request.json
    row = requst_object['message']
    print(row)
    res = resp(row)
    return json({'row': res},
                    status=200)


def routes(app: Sanic):
    app.add_route(process_message, '/bot', methods=['POST'])

 