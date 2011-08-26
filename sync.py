import urllib2
from urllib2 import HTTPError

import pyvo
import pygithub
import config

import json

vo = pyvo.VersionOne(config.vo_user, config.vo_pass)
github = pygithub.Github(config.gh_user, config.gh_pass)

stories = vo.get_stories()

for story in stories:
    try:
      post_data = { 'url': story.url, 'data': story.get_dict(), 'name': story.name, 'type':'VO_STORY' }
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

issues = github.get_repository("reach", "racker").get_issues(get_all=True)

for issue_num, issue in issues.items():
    try:
        post_data = { 'url': issue.url, 'data': issue.get_dict(), 'name': issue.title, 'type':'GH_ISSUE' }
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
