from luma.core.interface.parallel import bitbang_6800
from luma.core.render import canvas
from luma.oled.device import ws0010
import time
import requests

serial = bitbang_6800(RS=7, E=8, PINS=[25,24,23,27])

device = ws0010(serial,rotate=2, selected_font='FT01') # this font supports '£' sign

owned = 0.001337

while (True):
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    device.text = '!!! UPDATE !!!'
    currentPrice = data["bpi"]["GBP"]["rate_float"]
    toGbp = round(currentPrice * owned,2) 
    time.sleep(1)
    # other methods from the luma library doesn't seem to work with this particular screen
    device.text = '£' + str(data["bpi"]["GBP"]["rate"]) + '\n£' + str(toGbp)
    time.sleep(30)
