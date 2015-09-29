#!/usr/bin/python
import client as open_jub
import getpass
import mail_util
from expected_errors import *

if __name__ == '__main__':
  token = None

  while token == None:
    try:
      user = raw_input('Username: ')
      pwd = getpass.getpass()
      token = open_jub.login(user, pwd)
    except LoginException as e:
      print e

  print "Logged in! Token: %s" % token

  me = open_jub.current_user()
  sender = "fbi@fbi.gov"
  data = "Hey boo"
  title = "Test"

  print mail_util.send_mail(me, sender, data, title)
