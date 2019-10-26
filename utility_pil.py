from PIL import Image
from pylab import *
# read image to array
im = array(Image.open('./images/maracana1.jpg'))

row, col = im.shape[:2]

print(row)
print(col)
# plot the image
imshow(im)
# some points
x = [94, 182, 240, 158, 94]
y = [171, 126, 130, 175, 171]
# plot the points with red star-markers
plot(x,y,'r*')
# line plot connecting the first two points
plot(x,y)
# add title and show the plot
title('Plotting: "maracan1.jpg')
show()