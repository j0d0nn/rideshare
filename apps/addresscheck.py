import webapp2
import json
import cgi

from utils.utilities import UtilityMixin
from utils.requirelogin import RequireLoginMixin
from google.appengine.api import users

class AddressCheckAjax(webapp2.RequestHandler):
    
    def get(self, org):
        address = cgi.escape(self.request.get('address'))
        
        result = {
            'validated_address': 'yo'
        }
        result_json = json.dumps(result)
        self.response.headers['Content-Type'] = 'text/json'
        self.response.out.write(result_json)
        
