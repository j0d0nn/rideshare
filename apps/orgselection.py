import webapp2
import cgi

from utils.utilities import UtilityMixin, Organization
from utils.requirelogin import RequireLoginMixin
from google.appengine.api import users

class OrgSelectionPage(webapp2.RequestHandler, RequireLoginMixin, UtilityMixin):
    
    # handles the form post
    def post(self):
        key = cgi.escape(self.request.get('org'))
        # make sure the organization exists
        org = Organization.get_by_id(key)
        if org is None:
            self.invalid_input("The organization does not exist")
        else:
            self.redirect("/%s" % (key))
        
    
    def invalid_input(self, message):
        self.response.out.write(message)
        
    def render_page(self):
        user = users.get_current_user()
        orgs = Organization.get_all()
        print orgs[0].key
        template_values = {
            'name': user.nickname(),
            'orgs': orgs,
        }
        self.run_template('organizations.html', template_values)
