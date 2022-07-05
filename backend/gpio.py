from gpiozero import Button

def machine_IO_On():
    logging.info("IO On")

def machine_IO_Off():
    logging.info("IO Off")

button = Button(21)

button.when_pressed = machine_IO_on
button.when_released = machine_IO_Off

