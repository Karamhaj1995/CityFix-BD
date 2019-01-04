import tornado.web
import json
from server.models.database import User
from server.models.users import User as UserManager
from server.const.helptools import convert_arguments

class Api(tornado.web.RequestHandler):

    def get(self):
        data = convert_arguments(self.request.arguments)
        if data['method'] == "login":
            if UserManager().check_login(data):
                self.write(dict(user=json.loads(UserManager().check_login(data))))
            else:
                self.write(dict(user=json.loads('{"status":"Failed"}')))
        else:
            self.write(UserManager().users().to_json())

    def post(self):
        try:
            data = convert_arguments(self.request.arguments)
            self.write(dict(result=UserManager().create_user(data['name'], data['password'])))
        except Exception as e:
            self.write(dict(error=e))

    def delete(self):
        try:
            data = convert_arguments(self.request.arguments)
            print('wewewew')
            self.write(UserManager().delete_user(data['id']).to_json())
        except Exception as e:
            self.write(dict(error=e))