import time
import utime
import struct
import urandom
from ulora import TTN, uLoRa
from machine import Pin

# Refer to device pinout / schematics diagrams for pin details 
# (https://www.thethingsnetwork.org/forum/t/big-esp32-sx127x-topic-part-3/18436)
LORA_CS = const(18)
LORA_SCK = const(5)
LORA_MOSI = const(27)
LORA_MISO = const(19)
LORA_IRQ = const(26)
LORA_RST = const(14)
LORA_DATARATE = "SF7BW125" 
LED=Pin(2,Pin.OUT)

# As shown on TTN's dashboard
DEVICE_ADDRESS = bytearray([0x26, 0x01, 0x19, 0x70])
NETWORK_SESSION_KEY = bytearray([0xA4, 0x69, 0x94, 0x45, 0xCA, 0x7C, 0x12, 0x0A, 0x07, 0x8C, 0xE7, 0x7B, 0xB9, 0x23, 0x0E, 0x61])
APP_SESSION_KEY = bytearray([0x0B, 0x54, 0xC8, 0x3B, 0x78, 0x41, 0xE8, 0xAF, 0x96, 0x66, 0x3C, 0x9E, 0xC4, 0x12, 0x45, 0x39])
REGION="EU"

TTN_CONFIG = TTN(DEVICE_ADDRESS, NETWORK_SESSION_KEY, APP_SESSION_KEY, country=REGION)
FPORT = 1
lora = uLoRa(
    cs=LORA_CS,
    sck=LORA_SCK,
    mosi=LORA_MOSI,
    miso=LORA_MISO,
    irq=LORA_IRQ,
    rst=LORA_RST,
    ttn_config=TTN_CONFIG,
    datarate=LORA_DATARATE,
    fport=FPORT
)

while True:
    epoch = utime.time()
    temperature = urandom.randint(15,30)
    payload = struct.pack('@Qh', int(epoch), int(temperature))
    lora.send_data(payload, len(payload), lora.frame_counter)
    LED.value(1)
    time.sleep(1)
    LED.value(0)
    time.sleep(10)