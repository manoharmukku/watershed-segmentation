'''
Author: Manohar Mukku
Date: 05.12.2018
Desc: Watershed Segmentation algorithm
GitHub: https://github.com/manoharmukku/watershed-segmentation
'''

import sys
import cv2

def watershed(image):


def main(argv):
    # Read the input image
    img = cv2.imread(argv[0], 0)

    # Check if image exists or not
    if (img is None):
        print ("Cannot open {} image".format(argv[0]))
        print ("Make sure you provide the correct image path")
        sys.exit(2)

    # Perform segmentation using watershed on the input image
    segmented_image = watershed(img)

    # Print the segmented image
    cv2.imshow(segmented_image)

if __name__ == "__main__":
    main(sys.argv[1:])