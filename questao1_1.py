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

pixelPoints = array([array([p[1],p[0],0,1]) for p in points]).T
#worldPoints = array([[5.5, 5.5,0, 1],[18.32, 5.5, 0, 1],[16.5, 16.5, 0, 1],[40.32, 16.5, 0, 1]]).T
#worldPoints = array([[0, 0, 0, 1],[0, 0, 2.44, 1],[7.32, 0, 2.44, 1],[7.32, 0, 0, 1]]).T
worldPoints = array([[0, 0, 0], [2.79, 0, 0], [13.79, 0, 0], [19.29, 0, 0], [19.29, 0, 2.44],
                     [26.61, 0, 2.44], [26.61, 0, 0], [32.11, 0, 0], [43.11, 0, 0], [43.11, 16.5, 0]]).T
M = zeros((2 * pixelPoints.shape[1], 12))

M = calibrate(pixelPoints, worldPoints)
H = np.delete(M, 2, 1)

print("homography ", H)

pointSelected = ginput(1)
imgPoint = array([pointSelected[0][0],pointSelected[0][1],1])
inverseHom = linalg.inv(H)

worldVector = inverseHom.dot(imgPoint)
worldPoint = array([worldVector[0]/worldVector[2], worldVector[1]/worldVector[2], 1])

planeVector = H.dot(worldPoint)
planePointSelected = array([planeVector[0]/planeVector[2], planeVector[1]/planeVector[2]])

print('selected point', pointSelected)
print('world point', worldPoint)
print('reprojected point', planePointSelected)

playerPoint = array([worldPoint[0], worldPoint[1], 1.8])
playerVector = H.dot(playerPoint)
planePlayerPoint = array([playerVector[0]/playerVector[2], playerVector[1]/playerVector[2]])

print('player point ', planePlayerPoint)

x = [planePlayerPoint[0], pointSelected[0][0]]
y = [planePlayerPoint[1], pointSelected[0][1]]

# line plot connecting the first two points
plt.plot(x,y)
# add title and show the plot
plt.title('Plotting: "maracan1.jpg')
plt.show()




