from server.models.database import Location as LocationDB
from server.models.hazards import Hazard as HazardsManager

class Location():

	def location(self):
		return LocationDB.objects()

	def location_by_title(self, FA):
		return LocationDB.objects(FullAddress=FA)

	def create_location(self, **data):
		try:
			location = LocationDB(title=data['title'], location=data['location'], description=data['description'])
			location.commit(True) 
			return location.to_json()
		except Exception as e:
			return e

	def delete_location(self, id):
		location = LocationDB(pk=id)
		location.delete()
		return LocationDB.objects()