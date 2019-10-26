from pylab import *
from PIL import Image
import matplotlib.pyplot as plt
from scipy import linalg
import numpy as np
from dlt import *

imname = './images/maracana1.jpg'
im = array(Image.open(imname).convert('L'))

# mark corners
figure()
imshow(im)
gray()
points = ginput(10)

print(array([array([p[1],p[0],1]) for p in points]))

pixelPoints = array([array([p[1],p[0],0,1]) for p in points]).T
#worldPoints1 = array([[0, 0, 0, 1],[0, 0, 2.44, 1],[7.32, 0, 2.44, 1],[7.32, 0, 0, 1]]).T
worldPoints = array([[0, 0, 0], [2.79, 0, 0], [13.79, 0, 0], [19.29, 0, 0], [19.29, 0, 2.44],
                     [26.61, 0, 2.44], [26.61, 0, 0], [32.11, 0, 0], [43.11, 0, 0], [43.11, 16.5, 0]]).T

L = calibrate(pixelPoints, worldPoints)

print("Camera matrix ", L)

centerPoint = [159, 138, 0]
pointSelected = ginput(1)

print('selected point', pointSelected)

imgPoint = array([pointSelected[0][0],pointSelected[0][1],1])


customWorld = (imgPoint - centerPoint)

print('custom repo', L.dot([customWorld[0], customWorld[1],0,1]))

xyz = get_world_point(L, pointSelected[0][0], pointSelected[0][1])

print('world point', xyz)

worldVector = L.dot([xyz[0], xyz[1], xyz[2], 1])

print('reprojected', [worldVector[0]/worldVector[2], worldVector[1]/worldVector[2]])
planePlayerPoint = [worldVector[0]/worldVector[2], worldVector[1]/worldVector[2]]

x = [planePlayerPoint[0], pointSelected[0][0]]
y = [planePlayerPoint[1], pointSelected[0][1]]

# line plot connecting the first two points
plt.plot(x,y)
# add title and show the plot
plt.title('Plotting: "maracan1.jpg')
plt.show()



