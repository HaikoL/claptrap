#!/usr/bin/env python3

import logging
import logging.handlers
import sys
import os
import time

FILENAME="/baymax/logs/raspberry.log"

INFO = logging.INFO
ERROR = logging.ERROR

logger = logging.getLogger("baylog")
logger.setLevel(INFO)

handler = logging.handlers.TimedRotatingFileHandler(FILENAME, when="midnight", backupCount=7)
handler.setLevel(INFO)
formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')
handler.setFormatter(formatter)
handler .suffix = "%Y.%m.%d"
logger.addHandler(handler)

logger.info('Starting to log Raspberry Pi System')
logger.info('-- CPU -- Memory -- Voltage -- Temperatur --')

i = 1

while i == 1:

	temp = os.popen("vcgencmd measure_temp").readline().rstrip()
	mem = os.popen("free | awk 'FNR == 3 {print($3/($3+$4)*100)}'").readline().rstrip()
	volt = os.popen("vcgencmd measure_volts").readline().rstrip()
	cpu = os.popen("df -k / | tail -1 | awk '{print($5)}'").readline().rstrip()

	logger.info('	' + str(cpu) + '	' + str(mem) + '	' + str(volt) + '	' + str(temp))

	time.sleep(10)
