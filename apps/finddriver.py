import webapp2
import json
import cgi

from utils.utilities import UtilityMixin, Organization, Driver
from utils.requirelogin import RequireLoginMixin
from google.appengine.api import users
from google.appengine.ext import ndb

class FindDriverAjax(webapp2.RequestHandler, RequireLoginMixin, UtilityMixin):
    
    def get(self, org):
        nelat = float(cgi.escape(self.request.get('nelat')))
        nelng = float(cgi.escape(self.request.get('nelong')))
        swlat = float(cgi.escape(self.request.get('swlat')))
        swlng = float(cgi.escape(self.request.get('swlong')))

        # get all the drivers within these bounds
        drivers = Driver.get_by_bounds(org, nelat, nelng, swlat, swlng)
        
        result = [d.to_dict() for d in drivers]

        result_json = json.dumps(result)
        self.response.headers['Content-Type'] = 'text/json'
        self.response.out.write(result_json)
        
