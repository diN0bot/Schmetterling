#!/usr/bin/env python

import pyvo
import pygithub
import config

import json

import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'Schmetterling.settings'

import sys

sys.path.append(os.path.abspath(__file__ + '/../..'))

from data_store.models import Leaf

vo = pyvo.VersionOne(config.vo_user, config.vo_pass)
github = pygithub.Github(config.gh_user, config.gh_pass)

repo = github.get_repository('reach')

data = json.dumps(repo.get_dict())

leaf = Leaf(name=repo.name, data=data, type='GH_REPO', url=repo.url)
leaf.save()

issues = repo.get_issues(get_all=True)

for key, issue in issues.items():
    data = json.dumps(issue.get_dict())
    leaf = Leaf(name=issue.title, data=data, type='GH_ISSUE', url=issue.url)
    leaf.save()

pulls = repo.get_pull_requests(get_all=True)

for key, pull in pulls.items():
    data=json.dumps(pull.get_dict())
    leaf = Leaf(name=pull.title, data=data, type='GH_PULL', url=pull.url)
    leaf.save()
