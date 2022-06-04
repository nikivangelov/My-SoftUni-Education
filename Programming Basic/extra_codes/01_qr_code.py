import pyqrcode
import png
from pyqrcode import QRCode

address = 'https://www.mobile.bg/pcgi/mobile.cgi?act=4&adv=11646208965878133&slink=nrz2dp'
url = pyqrcode.create(address)
url.png('Ferrari.png', scale=8)