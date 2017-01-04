import urllib2,json
import random
import time
url = 'http://localhost/api.php'
for i in range(10):
	count = random.randint(1,15)
	for index in range(1,count):
		temp = "{0:.2f}".format(random.uniform(-45.0,45.0))
		postdata = {'last_measure': temp, 'sensor_name' : 'sensor' + str(index)}

		req = urllib2.Request(url)
		req.add_header('Content-Type','application/json')
		data = json.dumps(postdata)

		response = urllib2.urlopen(req,data)
		print response.read()
	time.sleep(5)
