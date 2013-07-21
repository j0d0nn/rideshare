import webapp2

from utils.utilities import UtilityMixin
from utils.requirelogin import RequireLoginMixin
from google.appengine.api import users

class GiveARidePage(webapp2.RequestHandler, RequireLoginMixin, UtilityMixin):
    
    def render_page(self):
        user = users.get_current_user()
        template_values = {
            'name': user.nickname(),
            'org': self.argument,
            'email': user.email(),
        }
        self.run_template('givearide.html', template_values)
