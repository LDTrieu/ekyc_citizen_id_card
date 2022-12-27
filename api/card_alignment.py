import cv2
from matplotlib import pyplot as plt
import numpy as np
from utils.alignment import *
from utils.find_nearest_box import NearestBox
import os
import time
import argparse
# from utils import detect_face


def getCenterRatios(img, centers):
    """
    Calculates the position of the centers of all boxes 
    in the ID card image and Unet Mask relative to the width and height of the image 
    and returns these ratios as a numpy array.
    """
    if(len(img.shape) == 2):
        img_h, img_w = img.shape
        ratios = np.zeros_like(centers, dtype=np.float32)
        for i, center in enumerate(centers):
            ratios[i] = (center[0]/img_w, center[1]/img_h)
        return ratios
    else :
        img_h, img_w,_ = img.shape
        ratios = np.zeros_like(centers, dtype=np.float32)
        for i, center in enumerate(centers):
            ratios[i] = (center[0]/img_w, center[1]/img_h)
        return ratios
