from sanic import Sanic
from sanic.response import file
from routes import routes


app = Sanic("IT_LAB")
app.static('/', 'public/index.html')

@app.get('/index.js')

async def sho(request):
    return await file('./dist/index.js', status= 200, mime_type='application/javascript')


app.static('/styles.css', 'public/styles.css')

routes(app)


app.config.FALLBACK_ERROR_FORMAT = "html"
app.config.DEBUG = True
app.run(port=3050)