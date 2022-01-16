#!/usr/bin/python

import cv2
import numpy as np

def segment(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    blue = cv2.inRange(image,  (0, 20, 100), (70, 255, 255))
    red = cv2.inRange(image, (180, 0, 0), (255, 95, 95))

    blue_segmented = cv2.bitwise_and(image, image, mask = blue)
    red_segmented = cv2.bitwise_and(image, image, mask = red)

    return red_segmented
    # segmented = cv2.bitwise_or(blue_segmented, red_segmented)
    # kernel = np.ones((10, 10), np.uint8)
    # dilated = cv2.dilate(segmented.copy(), kernel, iterations = 3)
    # eroded = cv2.erode(dilated.copy(), kernel, iterations = 5)
    # blurred = cv2.medianBlur(eroded, 7)

    # gray = cv2.cvtColor(blurred.copy(), cv2.COLOR_RGB2GRAY)
    # binary = cv2.threshold(gray.copy(), 80, 255, cv2.THRESH_BINARY)[1]
    # return binary 

def main():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not cap.isOpened():
        print("Cannot capture camera")
        raise IOError()

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Cannot read camera frame")
        
    
        image = segment(frame)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        cv2.imshow("frame", image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()