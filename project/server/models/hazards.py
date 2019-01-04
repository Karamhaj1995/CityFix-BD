from server.models.database import Hazard as HazardDB
from server.models.database import Location as LocationDB
from server.models.users import User as UsersManager

class Hazard():

	def hazards(self, limit=15):
		return HazardDB.objects().order_by('-datetime').limit(limit)

	def hazard_by_title(self, title):
		return HazardDB.objects(title=title)

	def create_hazard(self, **data):
		try:
			location = LocationDB(Lat=data['lat'], Lng=data['lng'], FullAddress=data['fulladdress'])
			location.commit(True)
			hazard = HazardDB(title=data['title'], location=location, description=data['description'])
			hazard.commit(True)
			return hazard.to_json()
		except Exception as e:
			return e

	def delete_hazard(self, id):
		hazard = HazardDB(pk=id)
		hazard.delete()
		return HazardDB.objects()