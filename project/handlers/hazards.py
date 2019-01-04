import tornado.web
import json
from server.models.database import Hazard
from server.models.hazards import Hazard as HazardManager
from server.models.users import User as UserManager
from server.const.helptools import convert_arguments

class Api(tornado.web.RequestHandler):

	def get(self):
		data = convert_arguments(self.request.arguments)
		hazards = []
		if data.get('limit',None) is not None:
			self.write(HazardManager().hazards(int(data['limit'])).to_json())
			return
		for hazard in HazardManager().hazards():
			hazard['lat'] = hazard['location']['Lat']
			hazard['lng'] = hazard['location']['Lng']
			hazards.append(hazard.to_json())

		self.write(dict(results=hazards))

	def post(self):
		try:
			data = convert_arguments(self.request.arguments)
			print(data)
			self.write(dict(result=HazardManager().create_hazard(**data)))
		except Exception as e:
			self.write(dict(error=e))
			
	def delete(self):
		try:
			data = convert_arguments(self.request.arguments)
			print('wewewew')
			self.write(HazardManager().delete_hazard(data['id']).to_json())
		except Exception as e:
			self.write(dict(error=e))