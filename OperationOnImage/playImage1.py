import numpy as np
import cv2 as cv


if __name__ == '__main__':
    img = cv.imread('../basic/pkg_bot014.jpg')
    px = img[100, 100]
    blue = img[100, 100, 0]
    img[100, 100] = [255, 255, 255]
    print(px)
    print(blue)
    print(img)
    # accssing RED value
    print(img.item(10, 10, 2))
    # modifying RED value
    print(img.itemset((10, 10, 2), 100))
    print(img.item(10, 10, 2))

    # cv.namedWindow('frame')
    # cv.imshow('image', img)
