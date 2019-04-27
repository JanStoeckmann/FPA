import numpy as np
import cv2
import sys

#noise.py img gauss/poisson

def noisy(noise_typ,image):
   if noise_typ == "gauss":
      gauss = np.random.normal(0,12,image.shape)
      noisy = image + gauss
      return noisy
   elif noise_typ == "poisson":
       noisy = np.random.poisson(image)
       return noisy

def main():
   img = cv2.imread("images/"+sys.argv[2])
   cv2.imwrite( "images/"+sys.argv[2][0:-4]+"-"+sys.argv[1]+"-noise.jpg",  noisy(sys.argv[1], img) )

if __name__ == "__main__":
   main()
