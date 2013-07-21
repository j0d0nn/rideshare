import webapp2
import re
import cgi

from utils.utilities import UtilityMixin, Organization
from utils.requirelogin import RequireAdminMixin
from google.appengine.api import users

class AdminOrgMaintenancePage(webapp2.RequestHandler, RequireAdminMixin, UtilityMixin):
    
    # form post handler
    def post(self):
        key = cgi.escape(self.request.get('key'))
        name = cgi.escape(self.request.get('name'))
        city = cgi.escape(self.request.get('city'))
        country = cgi.escape(self.request.get('country'))
        if not key or not re.match('^\w+$', key):
            self.invalid_input("Invalid key")
        elif not name:
            self.invalid_input("Invalid name")
        elif not city:
            self.invalid_input("Invalid city")
        elif not country or not re.match('^[A-Z]{2}$', country):
            self.invalid_input("Invalid country")
        else:
            self.save_org(key, name, city, country)
            self.success(key, name)
    
    def invalid_input(self, message):
        self.response.out.write("Organization not saved: %s" % (message))
    
    def success(self, key, name):
        self.response.out.write("Organization '%s' saved with key '%s'" % (name, key))
        
    def save_org(self, key, name, city, country):
        org = Organization()
        org.key = key
        org.name = name
        org.city = city
        org.country = country
        org.put()
        
    def render_page(self):
        user = users.get_current_user()
        orgs = Organization.get_all()
        template_values = {
            'name': user.nickname(),
            'orgs': orgs,
        }
        self.run_template('admin/orgmaintenance.html', template_values)
