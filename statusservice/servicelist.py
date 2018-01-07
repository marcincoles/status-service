"""ServiceList returns a list of available services to check the status on"""

import json
import falcon

class ServiceListResource(object):

    def on_get(self, req, resp):
        doc = { 
            "services": ["status"]
        }
        resp.body = json.dumps(doc, ensure_ascii=False)
        resp.status = falcon.HTTP_200

    def isUp(self):
        return True
