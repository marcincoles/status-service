# from .context import app
from statusservice.app import api
import statusservice.servicelist
def test_app_exists():
    assert api != None

def test_servicelist_isUp_returns_true():
    slist = statusservice.servicelist.ServiceListResource()
    assert slist.isUp() == True
