'''
Author: Manohar Mukku
Date: 06.12.2018
Desc: Watershed Segmentation algorithm
GitHub: https://github.com/manoharmukku/watershed-segmentation
'''

import sys
import cv2
import numpy

def neighbourhood(image, x, y):
    neighbour_reg_nums = {}
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i == 0 and j == 0):
                continue
            if (x+i < 0 or y+j < 0):
                continue
            if (neighbour_reg_nums.get(image[x+i][y+j]) == None):
                neighbour_reg_nums[image[x+i][y+j]] = 1
            else
                neighbour_reg_nums[image[x+i][y+j]] += 1

    keys = neighbour_reg_nums.keys().sort()

    if (keys[0] == -1):
        if (len(keys) == 1): # Separate region
            return -1
        elif (len(keys) == 2): # Part of another region
            return keys[1]
        else: # Watershed
            return 0
    else:
        if (len(keys) == 1): # Part of another region
            return keys[0]
        else: # Watershed
            return 0

def watershed_segmentation(image):
    # Create a list of pixel intensities along with their coordinates
    intensity_list = []
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            intensity_list.append((image[i][j], (i, j)))

    # Sort the list with respect to their pixel intensities, in ascending order
    intensity_list.sort()

    # Create an empty segmented_image numpy ndarray initialized to -1's
    segmented_image = numpy.full(image.shape, -1, dtype=int)

    # Iterate the intensity_list in ascending order
    region_number = 0
    for item in intensity_list:
        intensity = item[0]
        i = item[1][0]
        j = item[1][1]

        # Get the region number of the current pixel's region by checking its neighbouring pixels
        region_status = neighbourhood(segmented_image, i, j)

        if (region_status == -1): # Separate region
            region_number += 1
            segmented_image[i][j] = region_number
        elif (region_status == 0): # Watershed
            segmented_image[i][j] = 0
        else: # Part of another region
            segmented_image[i][j] = region_status

    # Return the segmented image
    return segmented_image


def main(argv):
    # Read the input image
    img = cv2.imread(argv[0], 0)

    # Check if image exists or not
    if (img is None):
        print ("Cannot open {} image".format(argv[0]))
        print ("Make sure you provide the correct image path")
        sys.exit(2)

    # Perform segmentation using watershed_segmentation on the input image
    segmented_image = watershed_segmentation(img)

    # Print the segmented image
    #cv2.imshow(segmented_image, 0)

if __name__ == "__main__":
    main(sys.argv[1:])