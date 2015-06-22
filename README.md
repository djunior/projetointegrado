# projetointegrado
Projeto Integration UFRJ 2015-1


Setup Raspberry Pi
OS: Raspian
Dependencias:
python 2.7
python-open (apt-get install python-opencv)
RPi.GPIO (apt-get install python-rpi.gpio)
build-essential python-dev (apt-get install build-essential python-dev)
Adafruit_Python_DHT (https://github.com/adafruit/Adafruit_Python_DHT.git)
python-picamera (apt-get install python-picamera)

Periféricos:
Sensor AM2303 (DHT22)
Camera PiCamera NoIR

wget https://bitbucket.org/MattHawkinsUK/rpispy-misc/raw/master/python/lcd_16x2.py

Scripts:
* variaveis de ambiente: /usr/local/etc/gosurf
* logs: /var/local/log/gosurf/
* script de log: /usr/local/bin/gosurf_logger.sh
* script de fotos: /usr/local/bin/gosurf_take_picture,sh
* script de medida e envio para o servidor: /usr/bin/gosurf_beach_reading
