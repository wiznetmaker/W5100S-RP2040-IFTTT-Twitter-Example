from usocket import socket
from machine import Pin,SPI
import network
import time
import urequests

#W5x00 chip init
def w5x00_init():
    spi=SPI(0,2_000_000, mosi=Pin(19),miso=Pin(16),sck=Pin(18))
    nic = network.WIZNET5K(spi,Pin(17),Pin(20)) #spi,cs,reset pin
    nic.active(True)
    nic.ifconfig(('192.168.11.30','255.255.255.0','192.168.11.1','8.8.8.8'))
    while not nic.isconnected():
        time.sleep(1)
        print(nic.regs())
    print(nic.ifconfig())
        
def main():
    w5x00_init()

    message = "https://maker.ifttt.com/trigger/post-tweet/with/key/YOUR_API_KEY_HERE?value1=Hello%20World"
    urequests.post(message)
    
if __name__ == "__main__":
    main()
