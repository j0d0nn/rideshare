from google.appengine.api import users

###
# Forces a login to proceed: Implementations require definition of render_page().
###
class RequireLoginMixin:
    argument = None
    
    def get(self, arg = None):
        self.argument = arg
        user = users.get_current_user()
        if user:
            if not self.is_authorized(user):
                self.abort(403)
            elif "render_page" in dir(self):
                self.render_page()
            else:
                self.response.out.write("render_page() not implemented")
        else:
            self.redirect(users.create_login_url(self.request.uri))
    
    # Designed to be overridden         
    def is_authorized(self, user):
        return True
    
    
class RequireAdminMixin(RequireLoginMixin):    
    def is_authorized(self, user):
        return user and users.is_current_user_admin()
