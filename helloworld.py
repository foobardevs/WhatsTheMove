import os
import webapp2
import urllib
import jinja2

#this connects the templates folder to the working file.
current_directory = os.path.dirname(os.path.realpath(__file__))
template_directory = os.path.join(current_directory,'templates' )



JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_directory),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render())

class SignUP(webapp2.RequestHandler):
	def get(self):
		template = JINJA_ENVIRONMENT.get_template('signUP.html')
		self.response.write(template.render())

class Login(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('logIn.html')
        self.response.write(template.render())

class UserPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('user.html')
        self.response.write(template.render())       

class Post(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('Post.html')
        self.response.write(template.render())

class test(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('photoTest.html')
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/SignUP', SignUP),
    ('/Login', Login),
    ('/User', UserPage),
    ('/Post', Post),
    ('/test', test)
], debug=True)