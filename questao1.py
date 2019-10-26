from pylab import *
from PIL import Image
import matplotlib.pyplot as plt
from scipy import linalg
import numpy as np
from dlt import *

imname = './images/maracana1.jpg'
im = array(Image.open(imname))

# mark corners
figure()
imshow(im)
gray()

points1 = ginput(4)
pixelPoints1 = []

for p in points1:
  pixelPoints1.append([p[1], p[0], 0, 1])

lines = []
calibrationX = []
calibrationY = []

for index in range(len(pixelPoints1)-1):
  calibrationX.append([ pixelPoints1[index][1], pixelPoints1[index+1][1]])
  calibrationY.append([ pixelPoints1[index][0], pixelPoints1[index+1][0]])

lines = []

for line in range(len(calibrationX)):
  plt.scatter(calibrationX[line], calibrationY[line], c='c')

pixelPoints1 = asarray(pixelPoints1).T

# calibration 1
worldPoints1 = array([[0, 0, 0], [0, 0, 2.44], [7.32, 0, 2.44], [7.32, 0, 0]]).T

#worldPoints1 = array([[0, 0, 0], [2.79, 0, 0], [13.79, 0, 0], [19.29, 0, 0], [19.29, 0, 2.44], [26.61, 0, 2.44], [26.61, 0, 0], [32.11, 0, 0], [43.11, 0, 0], [43.11, 16.5, 0]]).T

M = calibrate(pixelPoints1, worldPoints1)

print(M.shape)

H = getHomography(M)

selectedPoints = ginput(10)

print('selected points', selectedPoints)
print(len(selectedPoints))

xAxis = []
yAxis = []

for index in range(len(selectedPoints)):

  point = selectedPoints[index]
  point = array([point[1], point[0], 1]).T

  selectedXYZ = linalg.inv(H).dot(point)
  XYZVector = selectedXYZ[0]/selectedXYZ[2], selectedXYZ[1]/selectedXYZ[2]

  backPoint = array([XYZVector[0], XYZVector[1], 1.8, 1]).T
  backScreenVector = M.dot(backPoint)
  backScreen = backScreenVector[0]/backScreenVector[2], backScreenVector[1]/backScreenVector[2]

  xAxis.append([backScreen[1], point[1]])
  yAxis.append([backScreen[0], point[0]])

lines = []
for line in range(len(xAxis)):
  lines.append(plt.plot(xAxis[line], yAxis[line]))

plt.setp(lines, color='r')
plt.show()





