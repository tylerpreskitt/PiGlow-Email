#!/usr/bin/env python

import sys
import imaplib
import getpass
import email
import datetime

EMAIL_ACCOUNT = "akumaraspberry@gmail.com"
EMAIL_FOLDER = "Gmail"

def process_mailbox(M):
	
	rv, data = M.search(None, "ALL")
	if rv != 'OK':
		print "No messages found!"
		return
	
	for num in data[0].split():
		rv, data = M.fetch(num, '(RFC822)')
		if rv != 'OK':
			print "ERROR getting message", num
			return
		
		msg = email.message_from_string(data[0][1])
		decode = email.header.decode_header(msg['Subject'])[0]
		subject = unicode(decode[0])
		print 'Message %s: %s' % (num, subject)
		
M = imaplib.IMAP4_SSL('imap.gmail.com')

try:
	rv, data = M.login(EMAIL_ACCOUNT, getpass.getpass())
except imaplib.IMAP4.error:
	print "LOGIN FAILED!"
	sys.exit(1)
	
print rv, data

rv, mailboxes = M.list()
if rv == 'OK':
	print "Mailboxes:"
	print mailboxes
	
rv, data = M.elect(EMAIL_FOLDER)
if rv == 'OK':
	print "processing mailbox... \n"
	process_mailbx(M)
	M.close()
else:
	print "ERROR: Unable to open mailbox ", rv
	
M.logout()
