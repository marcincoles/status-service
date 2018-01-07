import falcon
from .things import ThingsResource
from .servicelist import ServiceListResource

api = application = falcon.API()

things = ThingsResource()
servicelist = ServiceListResource()

api.add_route('/', servicelist)
api.add_route('/things', things)
