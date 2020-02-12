from RPi import GPIO
import httplib
import urllib
import time
from time import sleep
key=" "         #Enter things speak key
begin=17
end=27
distance=10.0
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(begin,GPIO.IN)
GPIO.setup(end,GPIO.IN)
stime,etime=0,0
count=0
while(True):
    print "."
    while(True):
        if GPIO.input(begin)==GPIO.LOW:
            stime=time.time()
            break
    while(True):
        if GPIO.input(end)==GPIO.LOW:
            etime=time.time()
            speed=int(distance/(etime-stime))
            count=count+1
            break
    temp=int(open('/sys/class/thermal/thermal_zone0/temp').read())/1e3
    params=urllib.urlencode({'field1':temp,'field2':speed,'field3':count,'key':key})
    headers={"content-typZZe":"application/x-www-form-urlencoded","Accept":"text/plain"}
    conn=httplib.HTTPConnection("api.thingspeak.com:80")
    try:
	conn.request("POST","/update",params,headers)
	response=conn.getresponse()
	print str(temp)+" `C" 
	print str(speed)+" Km/hr" 
	print count
	conn.close()
    except:
	print "connection failed"
    sleep(20)
	
