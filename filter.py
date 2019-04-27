import cv2
import sys
import numpy as np

#filter.py img gauss/median/bilinear/meanshift

def smooth(filter, image):
    if filter == "gauss":
        smoothed = cv2.GaussianBlur(image,(5,5),cv2.BORDER_DEFAULT)
        return smoothed
    elif filter == "median":
        smoothed = cv2.medianBlur(image,5)
        return smoothed
    elif filter == "bilinear":
        smoothed = cv2.bilateralFilter(image,9,75,75)
        return smoothed

def main():
   img = cv2.imread("images/"+sys.argv[2])
   cv2.imwrite( "images/"+sys.argv[2][0:-4]+"-"+sys.argv[1]+"-filter.jpg",  smooth(sys.argv[1], img) )

if __name__ == "__main__":
   main()