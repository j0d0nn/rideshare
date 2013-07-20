import webapp2

from apps.home import HomePage
from apps.needaride import NeedARidePage
from apps.givearide import GiveARidePage
            
application = webapp2.WSGIApplication([
                 ('/', HomePage),
                 ('/needaride', NeedARidePage),
                 ('/givearide', GiveARidePage),
              ], debug=True)