import RPi.GPIO as GPIO
import time

# Define GPIO pin numbers
SW1 = 27
SW2 = 22

# Set up GPIO mode and pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        if GPIO.input(SW1) == GPIO.LOW:
            print("SW1 Pressed")
            time.sleep(0.5)  # Debounce delay
        elif GPIO.input(SW2) == GPIO.LOW:
            print("SW2 Pressed")
            time.sleep(0.5)  # Debounce delay
        time.sleep(0.1)  # Main loop delay
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nBye..")
