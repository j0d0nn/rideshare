from google.appengine.api import users

###
# Forces a login to proceed: Implementations require definition of render_page().
###
class RequireLoginMixin:
    
    def get(self):
        user = users.get_current_user()
        if user:
            if "render_page" in dir(self):
                self.render_page()
            else:
                raise AbstractMethodError("render_page() not implemented")
        else:
            self.redirect(users.create_login_url(self.request.uri))
             
class AbstractMethodError(Exception):
    pass