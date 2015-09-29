#!/usr/bin/python
"""
  Filename: config.python
  Parses the spammer settings
"""
import json
import sys

with open('settings.json') as settings_file:
  settings = json.load(settings_file)

if settings is None:
  raise Exception("Error parsing \"settings.json\". Make sure the file exists")

DEBUG = bool(settings['DEBUG'])
openJubUrl = str(settings['openJubUrl'])