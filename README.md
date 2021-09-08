# rpi-wifi-ledmatrix-conroller
A simple Flask-App for the RaspberryPi to controll a LED-Matrix with MAX-7219 chip via a nice web-interface. You can use it to draw your own pixel-image onto the matrix, display a rolling text message or display one of the example images on the LED-Matrix.

## How to use
### Required libraries:
* _luma.core_
* _luma.led-matrix_
* _pillow_
* _flask_

Please make sure these libraries are installed, so the programm can work accordingly.

---
### Connect the led-matrix to the RPI:
I made the following connections between my LED-Matrix and my RaspberryPi.
|Function   |Matrix Pin  |RPI Pin           |
|:---------:|:----------:|:----------------:|
|Power      |VCC         |3.3v              |
|Ground     |GND         |GND               |
|Data in    |DIN         |GPIO 10 (MOSI)    |
|Chip select|CS          |GPIO 8 (SPI CS0)  |
|Clock      |CLK         |GPIO 11 (SPI CLK) |

---
### Downloading and starting the App
1.  clone this repository onto your RPI and move into the folder
2.  start the _webapp_ledmatrix.py_
3.  open a webbrowser on any device within the same network of the RPI
    * Access the App with: `RPI_IP-Address`_:6060/led-matrix_
