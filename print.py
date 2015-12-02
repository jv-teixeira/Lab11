import boto
import urllib2

response = urllib2.urlopen('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key').read()
awskey = response.split(':')
print awskey[0]
print awskey[1]
print boto.Version
