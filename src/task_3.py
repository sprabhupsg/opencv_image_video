# Importing OpenCV Library
import cv2

# Relative or absolute path of the input image file
path = "C:\\opencv_image_video\\data\\checkerboard_18x18.png"

# reading image (by default the flag is 1 if not specidied)
image_gray = cv2.imread(path, 0)

print(image_gray)
print("image_gray.shape = ", image_gray.shape)
print("image_gray.size = ", image_gray.size)

image_gray[1,2] = 201
image_gray[2,3] = 202
image_gray[3,3] = 203
image_gray[4,0] = 204

print("modified image")
print(image_gray)

resized_2x = cv2.resize(image_gray,None,fx=2, fy=2)

print("resized_2x")
print(resized_2x)
print("resized_2x.shape = ", resized_2x.shape)
print("resized_2x.size = ", resized_2x.size)

# Wait until any key press (press any key to close the window)
cv2.waitKey()

# kill all the windows
cv2.destroyAllWindows()
