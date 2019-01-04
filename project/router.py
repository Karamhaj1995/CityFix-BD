from handlers.starter import MainHandler, LoginHandler, RegisterHandler
from handlers.profile import ProfileHandler
from handlers.users import Api as UserAPI
from handlers.hazards import Api as HazardsAPI
urls = [
		# web-pagging
		(r"/", MainHandler),
		(r"/login", LoginHandler),
		(r"/register", RegisterHandler),
		(r"/profile", ProfileHandler),
		# api-routing
		(r"/api/v1/users", UserAPI),
		(r"/api/v1/hazards", HazardsAPI)
	]