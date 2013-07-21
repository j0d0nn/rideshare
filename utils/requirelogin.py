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
    AUTHORIZED_USERS = ['j0d0nn', 'jodonn']
    
    def is_authorized(self, user):
        if user:
            nick = user.nickname()
            if nick in self.AUTHORIZED_USERS:
                return True
        return False