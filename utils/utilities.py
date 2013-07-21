import os

from google.appengine.ext.webapp import template
from google.appengine.ext import ndb

class UtilityMixin:
    
    def run_template(self, template_name, template_values):
        path = os.path.join(os.path.dirname(__file__), '../templates/' + template_name)
        self.response.out.write(template.render(path, template_values))

###
# Models an organization
###
class Organization(ndb.Model):
    key = ndb.StringProperty()
    name = ndb.StringProperty()
    city = ndb.StringProperty()
    country = ndb.StringProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
        
    @staticmethod
    def get_all():
        return Organization.query().order(Organization.name, Organization.city)
    
    @staticmethod
    def organization_key(key):
        return ndb.Key('key', key)
    