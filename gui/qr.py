import pyqrcode
import png
from pyqrcode import QRCode
  
  
  
def make(link):   
    s = link
    url = pyqrcode.create(s)
    
    url.png(f'qrcode.jpg', scale = 6)