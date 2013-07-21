import webapp2
import json
import cgi

from utils.utilities import UtilityMixin, Organization, Driver
from utils.requirelogin import RequireLoginMixin
from google.appengine.api import users
from google.appengine.ext import ndb

class SaveDriverAjax(webapp2.RequestHandler, RequireLoginMixin, UtilityMixin):
    
    def get(self, org):
        lat = float(cgi.escape(self.request.get('lat')))
        lng = float(cgi.escape(self.request.get('long')))
        seats = int(cgi.escape(self.request.get('seats')))
        user = users.get_current_user()
        user_id = user.user_id()
        email = user.email()

        # try to find the record to see if it should be created or updated
        driver = Driver.get_by_id(org, user_id)
        if driver is None:
            driver = Driver(parent = Organization.organization_key(org), id = user_id)
        driver.email = email
        driver.lat = lat
        driver.lng = lng
        driver.seats = seats
        driver.put()
        
        result = {
            'success': True
        }
        result_json = json.dumps(result)
        self.response.headers['Content-Type'] = 'text/json'
        self.response.out.write(result_json)
        
