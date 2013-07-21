import webapp2
import os

from utils.utilities import UtilityMixin
from utils.requirelogin import RequireLoginMixin
from google.appengine.api import users

class NeedARidePage(webapp2.RequestHandler, RequireLoginMixin, UtilityMixin):
    
    def render_page(self):
        user = users.get_current_user()
        template_values = {
            'name': user.nickname(),
            'org': self.argument,
        }
        self.run_template('needaride.html', template_values)
