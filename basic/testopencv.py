import cv2 as cv
import matplotlib.pyplot as plt


# img = cv.imread("pkg_bot014.jpg", cv.IMREAD_COLOR)  # picfile, read mode
img = cv.imread("pkg_bot014.jpg", cv.IMREAD_GRAYSCALE)  # picfile, read mode
# img = cv.imread("pkg_bot014.jpg", cv.IMREAD_UNCHANGED)  # picfile, read mode
print(type(img))  # numpy array
print(img.size)  # ndarray.size is an int object
print(img.shape)
# plt.imshow(img)
# plt.show()
cv.imshow("img", img)  # window_title, mat
cv.waitKey(0)  # you have to wait
cv.destroyAllWindows()
cv.imwrite("img_gray.jpg", img)
