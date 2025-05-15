import hal.hal_input_switch as switch
import hal.hal_led as led
from time import sleep

def init_mod():
    led.init()
    switch.init()

def blink_led(delay):
    # Led Blink
    led.init()

    led.set_output(0, 1) #on
    sleep(delay)
    led.set_output(0, 0) #off
    sleep(delay)
    led.set_output(0, 1) #on
    sleep(delay)
    led.set_output(0, 0) #off
    sleep(delay)

def main(): 
    init_mod()

    while True:
        if switch.read_slide_switch():
            print("Left")
            sleep(1.0)
            blink_led(0.2)
        else:
            for i in range(5):
                print("Right")
                blink_led(0.1)
                sleep(1.0)
            quit()
        
    return 0

if __name__ == "__main__":
    main()
