import httplib, urllib
import time
import smbus
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.cleanup
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

address = 0x48
A0 = 0x40
A1 = 0x41
A2 = 0x42
A3 = 0x43
bus = smbus.SMBus(1)

GPIO.setwarnings(False)
GPIO.cleanup
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
sleep = 10
key = ''

def thermometer():
	while True:
                bus.write_byte(address,A0)
                temp = bus.read_byte(address)
                currenttemp = temp*3.3*100/255
                ctemp = currenttemp*1.8+ 32
		params= urllib.urlencode({'field1': currenttemp, 'key':key })
		headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
		conn = httplib.HTTPConnection("api.thingspeak.com:80")

		try:
			conn.request("POST", "/update", params, headers)
			response = conn.getresponse()
			print "current temp in C: ", currenttemp
			print "current temp in F: ", ctemp
			print "http response: ", response.status, response.reason
			data = response.read()
			conn.close()
		except:
			print "connection failed"
		break

if __name__ == "__main__":
	while True:
		thermometer()
		time.sleep(sleep)







































