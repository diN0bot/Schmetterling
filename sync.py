import urllib2
from urllib2 import HTTPError

import pyvo
import pygithub

import json

vo = pyvo.VersionOne('', '')
github = pygithub.Github('', '')

sprints = vo.get_sprints()

for sprint in sprints:
    try:
      post_data = { 'url': sprint.url, 'data': sprint.get_dict(), 'name': sprint.name, 'type':'VO_ITERATION' }
      post_data = json.dumps(post_data)
      post_data = post_data.encode('ascii', 'ignore')
      url = 'http://127.0.0.1:8000/api/v1/leaf/'
      print post_data
      req = urllib2.Request(url, post_data, headers={'Content-Type':'application/json'})
      try:
          urllib2.urlopen(req)
      except HTTPError, e:
          print e.read()
          raise
    except:
        continue
