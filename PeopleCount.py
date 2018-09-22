import cv2

#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier('cascadeH5.xml')

image = cv2.imread('people2.jpg')
#grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#faces = face_cascade.detectMultiScale(grayImage)
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.CASCADE_SCALE_IMAGE
)

print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Faces found", image)
cv2.waitKey(0)

#
# print
# type(faces)
#
# if len(faces) == 0:
#     print
#     "No faces found"
#
# else:
#     print
#     faces
#     print
#     faces.shape
#     print
#     "Number of faces detected: " + str(faces.shape[0])
#
#     for (x, y, w, h) in faces:
#         cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 1)
#
#     cv2.rectangle(image, ((0, image.shape[0] - 25)), (270, image.shape[0]), (255, 255, 255), -1)
#     cv2.putText(image, "Number of faces detected: " + str(faces.shape[0]), (0, image.shape[0] - 10),
#                 cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0, 0, 0), 1)
#
#     cv2.imshow('Image with faces', image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()