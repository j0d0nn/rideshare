import webapp2

from utils.utilities import UtilityMixin, Driver
from utils.requirelogin import RequireLoginMixin
from google.appengine.api import users

class RemoveDriverPage(webapp2.RequestHandler, RequireLoginMixin, UtilityMixin):
    
    def render_page(self):
        user = users.get_current_user()
        template_values = {
            'name': user.nickname(),
            'org': self.argument,
            'email': user.email(),
        }
        self.run_template('removedriver.html', template_values)

    # form submit--do the submission
    def post(self, org):
        user = users.get_current_user()
        Driver.remove(org, user.user_id())
        