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
    name = ndb.StringProperty()
    city = ndb.StringProperty()
    country = ndb.StringProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
        
    @staticmethod
    def get_all():
        return Organization.query().order(Organization.name, Organization.city).fetch()
    
    @staticmethod
    def get_by_id(key):
        return Organization.organization_key(key).get()
    
    @staticmethod
    def organization_key(key):
        return ndb.Key(Organization, key)
    
class Driver(ndb.Model):
    email = ndb.StringProperty(indexed=False)
    lat = ndb.FloatProperty(indexed=False)
    lng = ndb.FloatProperty(indexed=False)
    seats = ndb.IntegerProperty(indexed=False)
    created = ndb.DateTimeProperty(auto_now_add=True)
    
    @staticmethod
    def get_by_id(org, id):
        return Driver.driver_key(org, id).get()
    
    @staticmethod
    def driver_key(org, id):
        return ndb.Key(pairs = [(Organization, org), (Driver, id)])