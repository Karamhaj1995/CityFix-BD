import jwt,time, datetime, json
from server.models.database import User as UserDB

class User():

	def users(self):
		return UserDB.objects()

	def user_by_name(self, name):
		return UserDB.objects(name=name)

	def create_user(self, username, password):
		try:
			user = UserDB(name=username)
			user.change_password(plain_password)
			extra['username'] = self.username
			extra['remote_ip'] = self.remote_ip                  
			user.commit(True)
			return user.to_json()            
		except:
			return dict(error='The user %s already exiest.' % username)

	def delete_user(self, id):
		user = UserDB(pk=id)
		user.delete()
		return UserDB.objects()

	def view_user_token(self,token):
		return jwt.decode(token, 'rWxHp4CBC8h0SiPY3gPKIGbed14bBCsj0VK8RQrrmKqa0ZveQvXNd7MI2twENvVJHq7vdYJHWPhLq5ONA8nr6bbZenANIrynBUEVbMHpMud3K8iUSAanfKTZ', algorithms='HS256')

	def set_user_token(self, username,password):
		user = UserDB.objects(name=username).first()
		if user is None:
			return False
		if user.check_user_pass(password):
			payload = {
				'username': user['name'],
				'_id': user['_id'],
				'remote_ip': self.request.remote_ip
			}
			return jwt.encode(payload, 'rWxHp4CBC8h0SiPY3gPKIGbed14bBCsj0VK8RQrrmKqa0ZveQvXNd7MI2twENvVJHq7vdYJHWPhLq5ONA8nr6bbZenANIrynBUEVbMHpMud3K8iUSAanfKTZ', algorithm='HS256')
		else:
			return False






