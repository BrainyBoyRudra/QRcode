import pyqrcode
import png
from pyqrcode import QRCode
s = "https://experiments.withgoogle.com/interplay-mode/view/"
url = pyqrcode.create(s)
url.svg('MYQR.svg',scale = 8)
url.png('MYQR.png',scale = 6)