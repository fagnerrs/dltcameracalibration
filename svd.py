import homography
from camera_matrix import dlt
from pylab import *
from PIL import Image
from scipy import linalg
import numpy as np

imname = './images/maracana1.jpg'
im = array(Image.open(imname).convert('L'))

# mark corners
figure()
imshow(im)
gray()
points = ginput(4)

print(array([array([p[1],p[0],1]) for p in points]))

pixelPoints = array([array([p[1],p[0],0,1]) for p in points]).T
worldPoints = array([[0,0,0, 1],[0, 0, 2.44, 1],[7.32, 0, 2.44, 1],[7.32, 0, 0, 1]]).T


#worldPoints = array([[0,0,0, 1],[0,5.5,0,1],[12.32,5.5,0,1],[12.32,0,0,1],
#                     [0,0,0, 1],[0, 0, 2.44, 1],[7.32, 0, 2.44, 1],[7.32, 0, 0, 1]]).T


M = zeros((2 * pixelPoints.shape[1], 12))

for pos in range(pixelPoints.shape[1]):
  x = worldPoints[0][pos]
  y = worldPoints[1][pos]
  z = worldPoints[2][pos]

  u = pixelPoints[0][pos]
  v = pixelPoints[1][pos]

  M[pos] = [x, y, z, 1, 0, 0, 0, 0, -u * x, -u * y, -u * z, -u]
  M[pos+1] = [0, 0, 0, 0, x, y, z, 1, -v * x, -v * y, -v * z, -v]

cls = lambda: print('\n'*100)
cls()

U,S,V = linalg.svd(M)

print(V)

M = V[8].reshape(3,4)
H = np.delete(M, 2, 1)

print("homography ", H)

pointSelected = ginput(1)
imgPoint = array([pointSelected[0][0],pointSelected[0][1],0, 1])
#inverseHom = linalg.inv(H)
inverseHom = M

worldVector = inverseHom.dot(imgPoint)
worldPoint = array([worldVector[0]/worldVector[2], worldVector[1]/worldVector[2], 0, 1])

planeVector = M.dot(worldPoint)
planePointSelected = array([planeVector[0]/planeVector[2], planeVector[1]/planeVector[2], 0, 1])

print('selected point', pointSelected)
print('world point', worldPoint)
print('reprojected point', planePointSelected)

# drawing player
playerPoint = array([worldPoint[0], worldPoint[1], 1.8, 1])
playerVector = M.dot(playerPoint)
planePlayerPoint = array([playerVector[0]/playerVector[2], playerVector[1]/playerVector[2]])

print('player point ', planePlayerPoint)


