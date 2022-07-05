from gpiozero import Button
import logging
from time import sleep

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("io.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

def machine_IO_On():
    logging.info("IO On")

def machine_IO_Off():
    logging.info("IO Off")

button = Button(21)
led = LED(20)

button.when_pressed = machine_IO_On
button.when_released = machine_IO_Off

while True:
    led.on();
    sleep(2)
    led.off()
    slee(2)
    
