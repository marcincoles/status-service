"""First WSGI service - things"""
import falcon
import json

class ThingsResource(object):
    def on_get(self, req, resp):
        doc = {"quote": "We like shiny things"}
        resp.body = json.dumps(doc, ensure_ascii=False)
        resp.status = falcon.HTTP_200
