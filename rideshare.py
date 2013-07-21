import webapp2

from apps.home import HomePage
from apps.needaride import NeedARidePage
from apps.givearide import GiveARidePage
from apps.orgselection import OrgSelectionPage
from apps.addresscheck import AddressCheckAjax

from apps.admin.orgmaintenance import AdminOrgMaintenancePage
            
application = webapp2.WSGIApplication([
                 # pages
                 (r'/(\w+)/needaride', NeedARidePage),
                 (r'/(\w+)/givearide', GiveARidePage),
                 (r'/orgselection', OrgSelectionPage),
                 (r'/(\w+)', HomePage),
                 (r'/', OrgSelectionPage),
                 
                 # ajax servlets
                 (r'/(\w+)/addresscheck', AddressCheckAjax),
                 
                 # admin stuff
                 (r'/admin/orgs', AdminOrgMaintenancePage),
              ], debug=True)