'''
Author: Manohar Mukku
Date: 06.12.2018
Desc: Watershed Segmentation algorithm
GitHub: https://github.com/manoharmukku/watershed-segmentation
'''

import sys
import cv2
import numpy

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

        # Get the status of the region of the current pixel by checking its neighbouring pixels
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