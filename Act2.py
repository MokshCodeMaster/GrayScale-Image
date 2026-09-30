import cv2 
image = cv2.imread('example.jpeg')
grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
resized_image = cv2.resize(grey_image, (244, 244))
cv2.imshow('Processed Image', resized_image)
key = cv2.waitKey(0)
if key == ord('s'):
    cv2.imwrite('Greyscale_resized_image.jpeg', resized_image)
    print("Image saved as Geryscale_resized_image.jpeg")
else:
    print("image not saved")
cv2.destroyAllWindows()
print(f"Processed Image Dimensions : {resized_image.shape}")
