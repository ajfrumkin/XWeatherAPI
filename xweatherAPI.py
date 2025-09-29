# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import urllib
import json
		
request = urllib.request.urlopen('https://data.api.xweather.com/conditions/summary/-21.290277,-46.691944?format=json&from=2024-01-01&to=2025-02-27&fields=loc,periods.dateTimeISO,periods.temp,periods.precip&client_id=XeCzuKlKs6Y7FShr4h0GJ&client_secret=UUgPhCbt0gQT9WUI4xTc84XjyYyI29LCweNx1p1U')
response = request.read()
json = json.loads(response)
if json['success']:
	print(json)
else:
	print("An error occurred: %s" % (json['error']['description']))
request.close()