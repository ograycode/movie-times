import urllib2
import simplejson
import datetime
import re
import sys


api_key = '6wghay7q2jcxhua7qhet42q6'
devider = '==================='

def get_movies(zip_code):
	base_url = 'http://data.tmsapi.com/v1/movies/showings?'
	start_date = datetime.datetime.now().strftime("%Y-%m-%d")
	zip_code = '20120'
	url = base_url + 'startDate=' + start_date + '&zip=' + zip_code + '&api_key=' + api_key
	results = simplejson.loads(urllib2.urlopen(url).read())
	return results

entry = ''
for arg in sys.argv:
	entry = entry + arg

if re.search('\d\d\d\d\d', entry):
	results = get_movies(entry)
	print 'Pick your movie:'
	print devider
	index = 0
	for movie in results:
		print str(index) + ': ' + movie['title']
		index = index + 1

	pick = raw_input('-->')

	picked = results[int(pick)]
	print devider
	print 'Playing at'
	print devider
	play_times = {}
	for showtime in picked['showtimes']:
		theatre = showtime['theatre']['name']
		time = showtime['dateTime']
		not_found = True
		for key in play_times.keys():
			if theatre == key:
				not_found = False
		if not_found:
			play_times[theatre] = time + " "
		else:
			play_times[theatre] = play_times[theatre] + time + " "

	for key in play_times.keys():
		print key + ' at ' + play_times[key]
