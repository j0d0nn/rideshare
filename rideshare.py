import webapp2

from apps.home import HomePage
from apps.needaride import NeedARidePage
from apps.givearide import GiveARidePage
from apps.orgselection import OrgSelectionPage
from apps.removedriver import RemoveDriverPage
from apps.finddriver import FindDriverAjax
from apps.savedriver import SaveDriverAjax

from apps.admin.orgmaintenance import AdminOrgMaintenancePage
            
application = webapp2.WSGIApplication([
                 # pages
                 (r'/(\w+)/needaride', NeedARidePage),
                 (r'/(\w+)/givearide', GiveARidePage),
                 (r'/(\w+)/removedriver', RemoveDriverPage),
                 (r'/orgselection', OrgSelectionPage),
                 (r'/(\w+)/', HomePage),
                 (r'/(\w+)', HomePage),
                 (r'/', OrgSelectionPage),
                 
                 # ajax servlets
                 (r'/(\w+)/finddriver', FindDriverAjax),
                 (r'/(\w+)/savedriver', SaveDriverAjax),
                 
                 # admin stuff
                 (r'/admin/orgs', AdminOrgMaintenancePage),
              ], debug=True)