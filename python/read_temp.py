import Adafruit_DHT as DHT


h,t = DHT.read_retry(DHT.DHT22,"14")

print "Temp: " + str(t) + " C"

print "Humidity: " + str(h) + " %"
