#!/usr/bin/python

class ConfigException(Exception):
  """
    Raised when an error occurs while parsing the settings
  """
  pass


class LoginException(Exception):
  """
    Unable to authenticate with OpenJUB
  """
  pass

