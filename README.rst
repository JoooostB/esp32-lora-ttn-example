Disclaimer
============

**This project is currently work in progress and there is no guarantee that it works as intended (in fact, it probably doesn't).**

Introduction
============

This is an experimental port of Adafruit's CircuitPython Tiny LoRa / LoRaWAN driver to MicroPython which allows IoT *things* to transmit light payloads to The Things Network (TTN).

Original Adafruit repository from which this project has been forked is available here:

https://github.com/adafruit/Adafruit_CircuitPython_TinyLoRa

Objecive
============

The aim is to enable LoRa / LoRaWAN capability on MicroPython ESP32 builds, using only minimal (and where possible) native MicroPython libraries.  By in large the code resembles the original, but where applicable, libraries and syntax has been adapted for MicroPython.

Being tested on
============

The project is currently being tested in a limited capacity using:

- HelTec Automation ESP32 LoRa development board V2, equipped with Semtech SX1276 module.  Pin out for this development board can be found here: https://github.com/Heltec-Aaron-Lee/WiFi_Kit_series/blob/master/PinoutDiagram/WIFI_LoRa_32_V2.pdf.
- The Things Network (TTN), with ABP Activation Method (more information on TTN setup: https://learn.adafruit.com/using-lorawan-and-the-things-network-with-circuitpython/tinylora-ttn-setup)

The premise of the port is that CircuitPython is equipped with a RF module with the *RFM* module.  As the LoRa component of the RFM module is based on a Semtech SX1276, all of the code relating to the SPI communication shuould be transferrable.

Further information on CircuitPython can be found here:

https://learn.adafruit.com/using-lorawan-and-the-things-network-with-circuitpython/overview

Usage example
============

Note that *DEVADDR*, *NWKEY* and *APP* are shown against your device in the TTN console (if ABP has been configured).

SX1276 module requires a number of standard SPI pins (CS, SCK, MOSI and MISO), as well as IRQ and RST.

code-block:: python
	import utime
	from ulora import TTN, uLoRa

	TTN_CONFIG = TTN(DEVADDR, NWKEY, APP, country="EU")
	lora = uLoRa(
        LORA_CS,
        LORA_SCK,
        LORA_MOSI,
        LORA_MISO,
        LORA_IRQ,
        LORA_RST,
        TTN_CONFIG
    )
    # data is a bytearray
    lora.send_data(data, len(data), lora.frame_counter)
    
Note that, throughout, the region (and therefore frequencies) defaults to "EU" unless explicitly specified.
