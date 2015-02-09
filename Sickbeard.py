#!/usr/bin/env python
# encoding: utf-8
import json
from urllib2 import Request, urlopen, URLError
import datetime

# your sickbeard settings go here:
sburl = '127.0.0.1'
sbport = '8081'
apikey = 'yourapikeyhere'

now = datetime.datetime.now()
day = now.strftime("%A")

request = Request('http://' + sburl + ':' + sbport + '/api/' + apikey + '/?cmd=future&sort=date&type=today|missed')

# shows you want to hide from displaying
keywords = ['Seriename']

try:
    response = urlopen(request)
    tv_shows = json.loads(response.read())
    for show_data in tv_shows['data']['missed']:
        if 'show_name' in show_data:
           if not any(word in show_data['show_name'] for word in keywords):
               print show_data['show_name']

    if day == "Sunday":
       print "Monday:"
    if day == "Monday":
       print "Tuesday:"
    if day == "Tuesday":
       print "Wednesay:"
    if day == "Wednesday":
       print "Thursday:"
    if day == "Thursday":
      print "Friday:"
    if day == "Friday":	
      print "Saturday:"
    if day == "Saturday":
      print "Sunday:"

    for show_data in tv_shows['data']['today']:
        if 'show_name' in show_data:
           if not any(word in show_data['show_name'] for word in keywords):
              print show_data['show_name']

except URLError, e:
    print ('Error')
