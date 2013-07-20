import webapp2

from utils.utilities import UtilityMixin
from utils.requirelogin import RequireLoginMixin
from google.appengine.api import users

class HomePage(webapp2.RequestHandler, RequireLoginMixin, UtilityMixin):
    
    def render_page(self):
        user = users.get_current_user()
        template_values = {
            'name': user.nickname(),
        }
        self.run_template('index.html', template_values)
