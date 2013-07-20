import os

from google.appengine.ext.webapp import template

class UtilityMixin:
    
    def run_template(self, template_name, template_values):
        path = os.path.join(os.path.dirname(__file__), '../templates/' + template_name)
        self.response.out.write(template.render(path, template_values))

