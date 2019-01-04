import tornado.web
import time , uuid
from server.models.users import User as UserManager

class CityFixReq(tornado.web.RequestHandler):
	
	token = {}

	def initialize(self):
        self.cur_token  = self.get_secure_cookie('auth')
        self.trans_id = str(uuid.uuid4())

	def get_current_user(self):
        if self.cur_token:
            self.token = User().view_user_token(self.cur_token)
            if (time.time() - self.token['issued']) > 3600:
                return None
            self.token['remote_ip'] = self.request.remote_ip
            return self.cur_token
        return None