#Author - Joao Victor Teixeira - Nov 15

import boto.sqs
import boto.sqs.queue
import urllib2

from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import sys

response = urllib2.urlopen('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key').read()
aswkey = response.split(':')

#Get te keys
access_key_id = aswkey[0]
secret_access_key = aswkey[1]

#Set up connection
conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=access_key_id,aws_secret_access_key=secret_access_key)

#Delete a queue
queue_name = sys.argv[1]
q = conn.get_queue(queue_name)
p = q.count()

print ('There are ' + str(p) + ' messages')

