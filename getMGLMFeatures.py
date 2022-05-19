# -*- coding: utf-8 -*-
"""
Readme: Count GLCM features from a image.
"""

import numpy as np
import cv2
from skimage.feature import greycomatrix, greycoprops


def getGLCMFeatures(impath):
    """
    :param impath: [string] path of image
    :return: [numpy.ndarray] a vector(32 len) represent feature of input image
    """

    image = cv2.imread(impath, 0)
    glcm = greycomatrix(image, distances=[1, 3], angles=[0, np.pi / 4, np.pi / 2, np.pi * 3 / 4],
                        levels=256, symmetric=False, normed=True)
    contrast = greycoprops(glcm, 'contrast')
    dissimilarity = greycoprops(glcm, 'dissimilarity')
    homogeneity = greycoprops(glcm, 'homogeneity')  # IDM
    ASM = greycoprops(glcm, 'ASM')
    ret = np.concatenate((contrast.flatten(), dissimilarity.flatten(), homogeneity.flatten(), ASM.flatten()))
    return ret


if __name__ == "__main__":
    imPath = "/Users/ferdinandd/Desktop/毕设/SEM_Image_Manager/SEM_Image/QP_zj_707.jpg"
    ret = getGLCMFeatures(imPath)
    print(ret)
    print(type(ret))
    print(type(ret[0]))
