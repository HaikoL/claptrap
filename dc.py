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


pwm.start(10)
print "10"
sleep(2)

pwm.ChangeDutyCycle(20)
print "20"
sleep(2)

pwm.ChangeDutyCycle(40)
print "40"
sleep(2)

pwm.ChangeDutyCycle(60)
print "60"
sleep(2)

pwm.ChangeDutyCycle(80)
print "80"
sleep(2)

pwm.ChangeDutyCycle(100)
print "100"
sleep(2)


print "Stopping Motor"
GPIO.output(DC1E, GPIO.LOW)

pwm.stop()
GPIO.cleanup()
