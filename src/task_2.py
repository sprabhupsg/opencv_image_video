# Importing OpenCV Library
import cv2

# Relative or absolute path of the input image file
path = "C:\\opencv_image_video\\data\\tom.jpg"

# reading image (by default the flag is 1 if not specidied)
image = cv2.imread(path)

# converting image to Grayscale (also OpenCV reads image in BGR format and hence BGR to Gray)
image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# Display image in a window
cv2.imshow("Gray Output",image_gray)

# Saving the image
cv2.imwrite('C:\\opencv_image_video\\data\\tom_gray.jpg',image_gray)

# Display image in a window
cv2.imshow("Output",image)

img_flipped_horz = cv2.flip(image, 1)
img_flipped_vert = cv2.flip(image, 0)
img_flipped_both = cv2.flip(image, -1)

# Display image in a window
cv2.imshow("img_flipped_horz",img_flipped_horz)

cv2.imshow("img_flipped_vert",img_flipped_vert)

cv2.imshow("img_flipped_both",img_flipped_both)

# Wait until any key press (press any key to close the window)
cv2.waitKey()

# kill all the windows
cv2.destroyAllWindows()
