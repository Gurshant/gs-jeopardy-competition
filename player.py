import RPi.GPIO as gpio

class Player():
    def __init__(self, button, light):
        gpio.setmode(gpio.BCM)

        #Setup pins and board
        self.button_pin = button
        self.light_pin = light

        gpio.setmode(gpio.BCM)
        gpio.setup(self.button_pin, gpio.IN, pull_up_down=gpio.PUD_UP)
        #TODO Combine these two lines under if possible
        gpio.setup(self.light_pin, gpio.OUT)
        gpio.output(self.light_pin, gpio.HIGH)

    def light_on(self):
        gpio.output(self.light_pin, gpio.LOW)
    
    def light_off(self):
        gpio.output(self.light_pin, gpio.HIGH)
        
    def input_from_button(self):
        return gpio.input(self.button_pin)
