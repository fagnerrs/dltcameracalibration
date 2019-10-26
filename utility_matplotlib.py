from PIL import Image
from pylab import *

im = array(Image.open('./images/maracana1.jpg'))
imshow(im)
print('Please click 4 points')

x = ginput(4)
print('you clicked:', x)
show()