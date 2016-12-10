import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

DC1A = 16
DC1B = 18
DC1E = 22

GPIO.setup(DC1A, GPIO.OUT)
GPIO.setup(DC1B, GPIO.OUT)
GPIO.setup(DC1E, GPIO.OUT)

pwm = GPIO.PWM(22, 100)

print "Turning motor ON"
GPIO.output(DC1A, GPIO.HIGH)
GPIO.output(DC1B, GPIO.LOW)
GPIO.output(DC1E, GPIO.HIGH)


pwm.start(95)
print "95% fuer 1 sec"
sleep(1)

print "Stopping Motor"
GPIO.output(DC1E, GPIO.LOW)

pwm.stop()
GPIO.cleanup()
