#klein
import json
from klein import Klein

class CandyStore(object):
    app = Klein()
    def __init__(self):
        self._items = {'Liquorice':10,'Spunk':8,'coins':2,'milka':18,'Gummi':9,'Ricola':16,'Aero':7,'Mars':7,'Skittles':3,'Smarties':2}

    @app.route('/')
    def items(self, request):
        request.setHeader('Content-Type','application/json')
        return json.dumps(self._items)

    @app.route('/<string:name>', methods=['PUT'])
    def save_item(self, request, name):
        request.setHeader('Content-Type','application/json')
        body = json.loads(request.content.read())
        self._items[name] = body
        return json.dumps({'success': True})

    @app.route('/<string:name>', methods=['GET'])
    def get_item(self, request, name):
        request.setHeader('Content-Type','application/json')
        return json.dumps(self._items.get(name))

if(__name__=='__main__'):
    store=CandyStore()
    store.app.run('localhost', 8080)