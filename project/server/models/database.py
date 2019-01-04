from server.const.db_conf import db_config
import os
import datetime
from mongoengine import *
from mongoengine import signals
from hashlib import sha512
from bson import json_util
import json

def connect_to_database():
	print('Connecting to database...(%s %s %s)' % (db_config['connection'],db_config['port'],db_config['dbname']))
	try:
		connect(db_config['dbname'], host=db_config['connection'], port=int(db_config['port']),username=db_config['dbusername'],password=db_config['dbpassword'])
	except:
		print("Problem to connect Ekron DB.")
	print("Connect to database was successful.")

connect_to_database()

class History(EmbeddedDocument):
	timestamp = DateTimeField(default=datetime.datetime.now())
	remote_ip = StringField()
	username = StringField()
	description = DictField()

class EkronBaseDocument(Document):
	
	modified = DateTimeField()
	created = DateTimeField(default=datetime.datetime.now())
	protected = BooleanField(default=False,required=True)
	history = EmbeddedDocumentListField(History)
	remote_ip = StringField()
	username = StringField()
	meta = {'abstract': True}

	def commit(self,new=False):

		if len(self._get_changed_fields()) == 0:
			if new:
				self.history.append(History(username=self.username,remote_ip=self.remote_ip,description={'Action':'Object Created'},timestamp=datetime.datetime.now()))
				self.save()
			return None
		changes = {}
		for change_field in self._get_changed_fields():
			changes[change_field] = str(self[change_field])
		self.history.append(History(username=self.username,remote_ip=self.remote_ip,description=changes,timestamp=datetime.datetime.now()))
		self.save()

	def __repr__(self):
		output = {}
		for f in self._fields_ordered:
				output[f] = getattr(self,f)
		return  str(output)

class User(EkronBaseDocument):
	name = StringField(required=True)
	password = StringField(required=True)
	salt_key = 'rWxHp4CBC8h0SiPY3gPKIGbed14bBCsj0VK8RQrrmKqa0ZveQvXNd7MI2twENvVJHq7vdYJHWPhLq5ONA8nr6bbZenANIrynBUEVbMHpMud3K8iUSAanfKTZ'
	meta = {'collection': 'Users'}
	
	def check_user_pass(self, password):
		try:
			hash_password, salt = self.password.split(':')
			result = hash_password == sha512(salt.encode() + password.encode()).hexdigest()
			return result
		except Exception as e:
			print(e)
			return False

	def change_password(self, password):
		self.password = sha512(self.salt_key.encode()+password.encode()).hexdigest() + ':' + self.salt_key

class Hazard(EkronBaseDocument):
	title = StringField()
	description = StringField()
	location = ReferenceField('Location')
	datetime = DateTimeField(default=datetime.datetime.now())
	lat = StringField()
	lng = StringField() 
	user = ReferenceField('User')
	meta = {'collection': 'Hazards'}

class Location(EkronBaseDocument):
	Lat = StringField(required=True)
	Lng = StringField(required=True)
	FullAddress = StringField(default='')
	meta = {'collection': 'Locations'}