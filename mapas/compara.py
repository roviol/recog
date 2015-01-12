import numpy as np
import cv2
from matplotlib import pyplot as plt
import sys
from drawobj import drawMatches
import json
from tempfile import TemporaryFile


img1 = cv2.imread(sys.argv[1],0)          # queryImage
img2 = cv2.imread(sys.argv[2],0) # trainImage

# Initiate SIFT detector
orb = cv2.ORB()

# find the keypoints and descriptors with SIFT
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)
#print dir(des1)
np.save("dest1", des1)
print des1.shape
# create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Match descriptors.
matches = bf.match(des1,des2)

# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)
#for match in matches:
#    print match.distance, match.trainIdx, match.queryIdx, match.imgIdx
# Draw first 10 matches.
#img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], flags=2)
#drawMatches(img1,kp1,img2,kp2,matches[:10])
#drawMatches(img1,kp1,img2,kp2,matches)
#plt.imshow(img3),plt.show()

