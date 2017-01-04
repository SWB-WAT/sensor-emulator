import urllib2,json
import random
import time
url = 'http://localhost/api.php'
temp = "{0:.2f}".format(random.uniform(-45.0,45.0))
postdata = {'last_measure': temp, 'sensor_name' : 'simple_sensor1'}

req = urllib2.Request(url)
req.add_header('Content-Type','application/json')
data = json.dumps(postdata)

response = urllib2.urlopen(req,data)
print response.read()
