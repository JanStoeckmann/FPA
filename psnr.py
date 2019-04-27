import numpy
import math
import cv2
import sys

def psnr(img1, img2):
    mse = numpy.mean( (img1 - img2) ** 2 )
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

def main():
   img1 = cv2.imread("images/"+sys.argv[1])
   img2 = cv2.imread("images/"+sys.argv[2])
   d = psnr(img1, img2)
   print(d)

if __name__ == "__main__":
   main()