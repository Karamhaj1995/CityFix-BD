import tornado.web
import tornado.ioloop
from server.models.database import User
from server.models.users import User as UserManager
from server.models.hazards import Hazard as HazardManager
from server.const.helptools import convert_arguments

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		parameters = {}
		parameters['latest_hazards'] = HazardManager().hazards()
		for hazard in parameters['latest_hazards']:
			hazard['lat'] = hazard['location']['Lat']
			hazard['lng'] = hazard['location']['Lng']
		self.render("index.html", parameters=parameters)

class LoginHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("login.html")

	def post(self):
		try:
			username, password = self.get_argument("username"), self.get_argument("password")
			print("%-20s username %s try to login." % (self.trans_id,username))          
			token = User().set_user_token(username,password)
			if not token:
			    print("%-20s username %s failed to login." % (self.trans_id,username))
			    self.render("Login.html", msg='badLoginCerd')
			    return
			self.set_secure_cookie('auth', token, expires_days=1)
			redirect_path = self.request.arguments.get('next',['/index'])
			self.redirect(redirect_path[0])
		except:
			self.render("Login.html", msg='Something wrong')

class RegisterHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("register.html")

	def post(self):
		try:
			data = convert_arguments(self.request.arguments)
			result=UserManager().create_user(data['name'], data['password'])
			if result['error']:
				return self.render("register.html")
			self.render("login.html", msg='Success')
		except Exception as e:
			self.write(dict(error=e))