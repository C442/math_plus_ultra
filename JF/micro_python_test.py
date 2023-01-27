from machine import Pin
from time import sleep

push_button_1 = Pin(13, Pin.IN,Pin.PULL_UP)
push_button_2 = Pin(13, Pin.IN,Pin.PULL_UP)
push_button_3 = Pin(13, Pin.IN,Pin.PULL_UP)
push_button_4 = Pin(13, Pin.IN,Pin.PULL_UP)
int_led = Pin(25,Pin.OUT)

print("start")

while True:
    logic_state = push_button.value()
    if logic_state == 1:
        int_led.value(1)
        print("Button 1 pressed")
    if logic_state == 0:
        int_led.value(0)

    print("Measure: "+ str(logic_state))
    
def checking_button(
#the idea is clear, now we should worry about the display