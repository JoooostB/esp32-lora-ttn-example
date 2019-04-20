Disclaimer
============

**Although successfully tested with limited functionality, this project is still currently work in progress and there is no guarantee that it works as intended.**

Introduction
============

This is an experimental port of Adafruit's CircuitPython Tiny LoRa / LoRaWAN driver to MicroPython which allows IoT *things* to transmit light payloads to The Things Network (TTN).

Original Adafruit repository from which this project has been forked is available here:

https://github.com/adafruit/Adafruit_CircuitPython_TinyLoRa

Objecive
============

The aim is to enable LoRa / LoRaWAN capability on MicroPython ESP32 builds, using only minimal (and where possible) native MicroPython libraries.  By in large the code resembles the original, but where applicable, libraries and syntax has been adapted for MicroPython.

Being tested on
===============

The project is currently being tested in a limited capacity using:

- HelTec Automation ESP32 LoRa development board V2, equipped with Semtech SX1276 module.  Pin out for this development board can be found here: https://github.com/Heltec-Aaron-Lee/WiFi_Kit_series/blob/master/PinoutDiagram/WIFI_LoRa_32_V2.pdf.
- The Things Network (TTN), with ABP Activation Method (more information on TTN setup: https://learn.adafruit.com/using-lorawan-and-the-things-network-with-circuitpython/tinylora-ttn-setup).
- Note that as is the case with the TinyLora library this has been forked from, it can only perform unconfirmed data up message type.

The premise of the port is that CircuitPython is equipped with a RF module, namely the *RFM9x* module.  As the LoRa component of the RFM module is based on a Semtech SX1276, all of the code relating to the SPI communication shuould be transferrable.

Further information on CircuitPython can be found here:

https://learn.adafruit.com/using-lorawan-and-the-things-network-with-circuitpython/overview

Usage example
=============

Note that *DEVADDR*, *NWKEY* and *APP* are shown against your device in the TTN console (if ABP has been configured).

SX1276 module requires a number of standard SPI pins (CS, SCK, MOSI and MISO), as well as IRQ and RST.
    
.. code-block:: python

    import utime
    from ulora import TTN, uLoRa
    # Refer to device pinout / schematics diagrams for pin details
	LORA_CS = const(18)
	LORA_SCK = const(5)
	LORA_MOSI = const(27)
	LORA_MISO = const(19)
	LORA_IRQ = const(26)
	LORA_RST = const(14)
	LORA_DATARATE = "SF9BW125"	# Choose from several available
	# From TTN console for device
	DEVADDR = bytearray([0x00, 0x00, 0x00, 0x00])
	NWKEY = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
	                   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
	APP = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
	                 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    TTN_CONFIG = TTN(DEVADDR, NWKEY, APP, country="EU")
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
    # ...Then send data as bytearray
    lora.send_data(data, len(data), lora.frame_counter)

Note that, throughout, the region (and therefore frequencies) defaults to "EU" unless explicitly specified.