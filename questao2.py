from pylab import *
from PIL import Image
import matplotlib.pyplot as plt
from scipy import linalg
import numpy as np
from dlt import *

imname = './images/maracana2.jpg'
im = array(Image.open(imname))

# mark corners
figure()
imshow(im)
gray()
#points = ginput(7)


#pixelPoints = array([array([p[1],p[0],0,1]) for p in points]).T

points1 = ginput(6)
pixelPoints1 = []

for p in points1:
  pixelPoints1.append([p[1], p[0], 0, 1])

lines = []
calibrationX = []
calibrationY = []

for index in range(len(pixelPoints1)-1):
  calibrationX.append([pixelPoints1[index][1], pixelPoints1[index+1][1]])
  calibrationY.append([pixelPoints1[index][0], pixelPoints1[index+1][0]])

lines = []

for line in range(len(calibrationX)):
  plt.scatter(calibrationX[line], calibrationY[line], c='c')

pixelPoints1 = asarray(pixelPoints1).T
#calibragem 1
#worldPoints1 = array([[0, 0, 0], [11, 0, 0], [11, 16.5, 2.44], [40.32, 16.5, 0]]).T

worldPoints1 = array([[0, 0, 0],[11, 0, 0], [18.32, 0, 0], [29.32, 0, 0],[29.32, 11, 0], [40.2,11, 0]]).T

#L = calibrate(pixelPoints, worldPoints)
M = calibrate(pixelPoints1, worldPoints1)

#print("Camera matrix ", L)

centerPoint = [159, 138, 0]

H = getHomography(M)

imgPoints = ginput(1)

xAxis = []
yAxis = []

for index in range(len(imgPoints)):
  imgPoint = imgPoints[index]

  print('sel', imgPoint)
  imgPoint = array([imgPoint[1], imgPoint[0], 1]).T

  w3Vector = linalg.inv(H).dot(imgPoint)

  w3 = array([(w3Vector[0]/w3Vector[2]) - 22.95, w3Vector[1]/w3Vector[2], 1])
  w4 = array([(w3Vector[0]/w3Vector[2]) + 22.95, w3Vector[1]/w3Vector[2], 1])

  r3Vector = H.dot(w3.T)
  r4Vector = H.dot(w4.T)

  r3 = array([r3Vector[0]/r3Vector[2], r3Vector[1]/r3Vector[2], 1])
  r4 = array([r4Vector[0]/r4Vector[2], r4Vector[1]/r4Vector[2], 1])

  xAxis.append([r3[1], r4[1]])
  yAxis.append([r3[0], r4[0]])

lines = []
for line in range(len(xAxis)):
  lines.append(plt.plot(xAxis[line], yAxis[line]))

plt.setp(lines, color='r')
plt.show()








