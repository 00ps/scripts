#!/usr/bin/env python

'''
uses Amazon SES to send bulk emails

fred badel <fred@never-mind.ch>
'''

import boto.ses
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# configure the boto connection
# if not set boto will attempt to read you
# ~/.boto file
region = "us-east-1"
key_id = "SOMEKEYID"
secret_key = "SOMESECRETKEY"

# Sender and subject of the email message
sender = "SENDER NICE NAME <do_not_reply@email.com>"
subject = "This is a bulk email sent via SES"

# plain text content of the mail:
# reads msg.txt in the current directory
ft = open('msg.txt', 'r')
txt = ft.read()

# html content of the mail:
# reads msg.html in the current directory
fh = open('msg.html', 'r')
html = fh.read()

# creates a boto connection using above credentials
conn = boto.ses.connect_to_region(
    region,
    aws_access_key_id=key_id,
    aws_secret_access_key=secret_key)

# read the list of recipients
rcptlist = open('clientList.txt', 'r')

# loop over the list provided above
for rcpt in rcptlist:
    # create a MIME message
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = rcpt
    msg.attach(MIMEText(txt, 'plain'))
    msg.attach(MIMEText(html, 'html'))

    # sends the message
    conn.send_raw_email(msg.as_string())

# print some information about your AWS SES Status
print "SES quota:"
print json.dumps(conn.get_send_quota(), indent=4, separators=(',', ': '))
print ""
print "SES statistics:"
print json.dumps(conn.get_send_statistics(), indent=4, separators=(',', ': '))
