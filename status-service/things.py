"""First WSGI service - things"""
import falcon

class ThingsResource(object):
	def on_get(self, req, resp):
		"""Handle GET requests for things"""
		resp.status = falcon.HTTP_200
		resp.body = ('\nWe all want things we do not have\n')

# falcon.API instances are callable WSGI apps
app = falcon.API()

# resources are long-lived class instances
things = ThingsResource()

app.add_route('/things', things)
