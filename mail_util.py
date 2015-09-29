#!/usr/bin/python
import telnetlib

KEYWORD_FIRST_NAME = "%%FIRSTNAME%%"
KEYWORD_LAST_NAME = "%%LASTNAME%%"
KEYWORD_EMAIL = "%%EMAIL%%"
KEYWORD_USERNAME = "%%USERNAME%%"
KEYWORD_MAJOR = "%%MAJOR%%"
KEYWORD_COUNTRY = "%%COUNTRY%%"

JACOBS_SMTP_ADDRESS = "exchange.jacobs-university.de"
TELNET_PORT = 25
MAIL_QUEUED = "Queued mail for delivery"

def send_mail(recepient, sender, email, title = None):
  email.replace(KEYWORD_FIRST_NAME, recepient.first_name)
  email.replace(KEYWORD_LAST_NAME, recepient.last_name)
  email.replace(KEYWORD_EMAIL, recepient.email)
  email.replace(KEYWORD_USERNAME, recepient.username)
  email.replace(KEYWORD_MAJOR, recepient.major)
  email.replace(KEYWORD_COUNTRY, recepient.country)

  if title == None:
    title = "Email from %s" % sender

  telnet = telnetlib.Telnet()
  telnet.open(JACOBS_SMTP_ADDRESS, TELNET_PORT)
  telnet.write("helo mailserver.jacobs--university.de\r\n")
  telnet.write("mail from: %s\r\n" % sender)
  telnet.write("rcpt to:%s\r\n" % recepient.email)
  telnet.write("data\r\n")
  telnet.write("Subject: %s\r\n\r\n" % title)
  telnet.write(email)
  telnet.write("\r\n.\r\n")
  telnet.write("quit\r\n")
  response = telnet.read_until(expected=MAIL_QUEUED, timeout=10)
  # READ RESPONSE!!
  telnet.close()

  return MAIL_QUEUED in response