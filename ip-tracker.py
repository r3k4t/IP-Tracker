
import urllib, json,os,sys
os.system("clear")
os.system("figlet  -f standard  IP Tracker")
print
print "Author : Rahat Khan Tusar(RKT)"
print
print "Github : https://github.com/r3k4t "
print
print "Information : This program can track any public ip and website ip address."
print 
ip = raw_input("Target IP :")
print 
url = 'http://ip-api.com/json/'
response = urllib.urlopen(url + ip)
data = response.read()
rkt = json.loads(data)
print

print (data)
print
print ('Done')
print
