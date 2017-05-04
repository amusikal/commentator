import falcon
import json


api = application = falcon.API()


class Resource(object):

    def on_get(self, req, resp):
        doc = {
            'obj': 'foo',
            'other': [1, 2, 3, 4]
            }

        # Create a JSON representation of the resource.
        resp.body = json.dumps(doc, ensure_ascii=False)
        resp.status = falcon.HTTP_200


resources = Resource()
api.add_route('/resources', resources)
