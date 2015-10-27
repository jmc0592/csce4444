# Test file for python parse object creation
# Author: Jacob Cole

execfile("../../pythonParseConnect.py") # alternative to import for file in different directory
from parse_rest.datatypes import Object, GeoPoint
from parse_rest.core import ParseError


# intialization
class Restaurant(Object):
    pass

restaurant = Restaurant(name="Los Pollos Hermanos")
# coordinates as floats.
restaurant.location = GeoPoint(latitude=12.0, longitude=-34.45)

try:
	restaurant.save();
	restaurants = restaurant.Query.all()
	for res in restaurants:
		print res.objectId
except ParseError:
	print 'Failed to create new object, with error message: '
