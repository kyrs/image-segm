#code from Htiango/Image-Segmentation
#https://github.com/Htiango/Image-Segmentation/blob/master/main/process_ground_truth.py

import scipy.io
import numpy as np

def get_groundTruths(path):
    """
    return the nparray of boundary (0 for boundary and 255 for area)
    :param path:
    :return:
    """
    mat = scipy.io.loadmat(path)
    groundTruth = mat.get('groundTruth')
    label_num = groundTruth.size
    boundaries = []

    for i in range(label_num):
        trueBoundary = groundTruth[0][i]['Boundaries'][0][0]

        height = trueBoundary.shape[0]
        width = trueBoundary.shape[1]
        trueBoundary = trueBoundary.reshape(height, width, 1)

        #trueBoundary = 255 * np.ones([height, width, 1], dtype="uint8") - (trueBoundary > 0) * 255
        
        boundaries.append(trueBoundary)

    return boundaries


def get_groundTruth(path):
    """
    return the nparray of boundary (0 for boundary and 255 for area)
    :param path:
    :return:
    """
    mat = scipy.io.loadmat(path)
    groundTruth = mat.get('groundTruth')
    label_num = groundTruth.size

    for i in range(1): #label_num):
        boundary = groundTruth[0][i]['Boundaries'][0][0]
        if i == 0:
            trueBoundary = boundary
        else:
            trueBoundary += boundary

    height = trueBoundary.shape[0]
    width = trueBoundary.shape[1]
    trueBoundary = trueBoundary.reshape(height, width, 1)

    trueBoundary = 255 * np.ones([height, width, 1], dtype="uint8") - (trueBoundary > 0) * 255

    return trueBoundary


# get_groundTruth('../data/groundTruth/train/2092.mat')