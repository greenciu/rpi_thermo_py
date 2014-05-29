rpi_thermo_py
=============

Sample project for retrieving data from RaspberryPI, storing and visualizing it using ELK stack.

### Description

The data collected from rpi is retrieved from a temperature sensor installed on the board.

We have a python script logging the data retrieved from the sensor. Another process is sending the data over to LogStash server. The data is filtered/manipulated and persisted in ElasticSearch. Kibana is then used to visualize the data.

### Installation steps

To deploy the script on the Pi install the following prerequisites:


`sudo apt-get update`

`sudo apt-get install python-dev`


Edit the raspi-blacklist.conf and uncomment the line: blacklist i2c-bcm2708, then restart

`sudo nano /etc/modprobe.d/raspi-blacklist.conf`

`sudo reboot`


Install the spidev module

`mkdir -p python-spi`

`cd python-spi/`

`wget https://raw.github.com/doceme/py-spidev/master/setup.py`

`wget https://raw.github.com/doceme/py-spidev/master/spidev_module.c`

`sudo python setup.py install`


Install and configure git

`sudo apt-get install git`

`git config --global credential.helper cache`

`git config --global credential.helper "cache --timeout=3600"`


Deploy the code

`git clone https://github.com/cubiks/rpi_thermo_py.git`


Run the script

`chmod +x temp.py `

`python temp.py`


For installing ELK stack instructions refer to: https://github.com/cubiks/rpi_thermo_py/wiki/Install-ELK-stack
