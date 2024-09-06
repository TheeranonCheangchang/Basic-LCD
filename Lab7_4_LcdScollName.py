import drivers
from time import sleep
import RPi.GPIO as GPIO
import time
import sys

display = drivers.Lcd()
display.lcd_clear()
SW1 = 27
SW2 = 22

lcd_position = 0
lcd_code = 0
count =1
names = ["Damrong","Athikorn","Theeranon"]
codestudents = ["116630462027-9","116630462013-9","116630462042-8"]


GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW2, GPIO.IN,pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(SW1,GPIO.FALLING)
GPIO.add_event_detect(SW2,GPIO.FALLING)

try:
    while True:
        if GPIO.event_detected(SW1):
            lcd_position += 1
            if lcd_position == 1 :
                display.lcd_display_string(names[lcd_position-1],1)
                display.lcd_display_string(codestudents[lcd_position-1],2)
                
                
            elif lcd_position == 2 :
                display.lcd_display_string(names[lcd_position-1],1)
                display.lcd_display_string(codestudents[lcd_position-1],2)
                
                
            elif lcd_position == 3 :
                display.lcd_display_string(names[lcd_position-1],1)
                display.lcd_display_string(codestudents[lcd_position-1],2)
                   
            else:
                lcd_position = 0
                display.lcd_clear()
        elif GPIO.event_detected(SW2):
            display.lcd_clear()
            print("\nBye...")
            exit()       
        time.sleep(0.5)

        

except KeyboardInterrupt:
    display.lcd_clear()
    print("\nBye...")