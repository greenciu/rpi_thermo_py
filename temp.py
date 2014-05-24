import spidev
import time
import logging
import logging.config
import json

logging.config.fileConfig("config/logging.json")
logger = logging.getLogger("temp")

spi = spidev.SpiDev()
spi.open(0,0)

def readadc(adcnum):
    if ((adcnum > 7) or (adcnum < 0)):
        return -1
    r = spi.xfer2([1,(8+adcnum)<<4,0])
    adcout = ((r[1]&3) << 8) + r[2]
    return adcout

adcInput = 0 # Pin 0
logger.info("Reading temperature level from pin-0 :")

while True:
    value = readadc(adcInput)
    voltage = value * 3.3
    voltage /= 1024.0
    tempCelsius = (voltage-0.5)*100
    logger.info("Temp: %f", tempCelsius)
    time.sleep(2)

