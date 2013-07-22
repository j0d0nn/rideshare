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
    lat = ndb.FloatProperty(indexed=True)
    lng = ndb.FloatProperty(indexed=True)
    seats = ndb.IntegerProperty(indexed=False)
    created = ndb.DateTimeProperty(auto_now_add=True)
    
    def to_dict(self):
        return { 
            'email': self.email,
            'lat': self.lat,
            'lng': self.lng,
            'seats': self.seats
        }
        
    @staticmethod
    def get_by_bounds(org, nelat, nelng, swlat, swlng):
        # ndb doesn't support inequality queries on more than one property, so we'll start with the lats and then
        # filter on the longs as they come in
        qry = Driver.query(ancestor = Organization.organization_key(org))
        
        # it'd be better to do the filter here, but I can't get it to work
        drivers = qry.fetch()

        # now filter the longs
        drivers = [d for d in drivers if d.lng > swlng and d.lng < nelng and d.lat > swlat and d.lat < nelat]
        return drivers
    
    @staticmethod
    def get_by_id(org, id):
        return Driver.driver_key(org, id).get()
    
    @staticmethod
    def driver_key(org, id):
        return ndb.Key(pairs = [(Organization, org), (Driver, id)])
    
