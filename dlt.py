from pylab import *

def calibrate(pixelPoints, worldPoints):

  M = []

  for pos in range(pixelPoints.shape[1]):
    x = worldPoints[0][pos]
    y = worldPoints[1][pos]
    z = worldPoints[2][pos]

    u = pixelPoints[0][pos]
    v = pixelPoints[1][pos]

    M.append([x, y, z, 1, 0, 0, 0, 0, -u * x, -u * y, -u * z, -u])
    M.append([0, 0, 0, 0, x, y, z, 1, -v * x, -v * y, -v * z, -v])

  M = asarray(M)
  [U, S, V] = linalg.svd(M)

  cameramatrix = V[-1,:]

  return cameramatrix.reshape(3,4);


def getHomography(cameraMatrix):
  return [[cameraMatrix[0][0], cameraMatrix[0][1], cameraMatrix[0][3]],
          [cameraMatrix[1][0], cameraMatrix[1][1], cameraMatrix[1][3]],
          [cameraMatrix[2][0], cameraMatrix[2][1], cameraMatrix[2][3]]]


