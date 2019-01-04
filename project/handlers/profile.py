import tornado.web

class ProfileHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("register.html", parameters={"Users": ""})