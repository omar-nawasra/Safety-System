from gpiozero import LED
from gpiozero import Button
from gpiozero import Buzzer 
from gpiozero import LineSensor
from gpiozero import DistanceSensor
from mpu6050 import mpu6050
import time
import math

mpu = mpu6050(0x68)
us = DistanceSensor(echo=18, trigger=17)
ir = LineSensor(4)
buzzer = Buzzer(5)
led = LED(23)
button = Button(6)

system_armed = False

while True:
    if button.is_pressed:
        system_armed = not system_armed 
        
        if system_armed == False:
            led.off()
            buzzer.off()
            print("System Deactivated")
        else:
            print("System Activated")
            
        time.sleep(0.5) 
        
    if system_armed == True:
        accel_data = mpu.get_accel_data()
        ax = accel_data['x']
        ay = accel_data['y']
        az = accel_data['z']
        
        magnitude = math.sqrt(ax**2 + ay**2 + az**2)
        
        print(f"Ultrasonic: {us.distance:.2f}m")
        print(f"IR Sensor: {ir.line_detected}")
        print(f"IMU Magnitude: {magnitude:.2f}")

        if us.distance < 2.0:
            if magnitude > 20.0:  
                led.blink(on_time=0.5, off_time=0.5)
            else:
                led.on()
        else:
            led.off()

        if ir.line_detected:
            buzzer.on()
            led.blink(on_time=0.1, off_time=0.1) 
        else:
            buzzer.off()

    time.sleep(0.1)
"""
from gpiozero import LED
from gpiozero import PWM
from gpiozero import Button
from gpiozero import Buzzer 
from gpiozero import LineSensor
from signal import pause
from gpiozero import DistanceSensor
import time
import math
import board
import busio
import adafruit_mpu6050
i2c = busio.I2C(board.SCL, board.SDA)
mpu = adafruit_mpu6050.MPU6050(i2c)
us = DistanceSensor(echo=17, trigger=4)
ir = LineSensor(5)
buzzer = Buzzer(18)
led = LED(27)
button = Button(22)
while True:
    ax, ay, az = mpu.acceleration
    magnitude = math.sqrt(ax**2 + ay**2 + az**2)

    if us.distance < 2.0:
        led.on()
        if magnitude > 20.0:  
            led.blink(on_time=0.5, off_time=0.5)
        elif button.is_pressed:
            led.off()
            buzzer.off()
            break
    elif button.is_pressed:
        led.off()
        buzzer.off()
        break
    else :
        led.off()
        buzzer.off() 

    if ir.line_detected:
                buzzer.on()
                time.sleep(1)
                buzzer.off()
                if button.is_pressed:
                    led.off()
                    buzzer.off()
                    break
"""
            
            
        