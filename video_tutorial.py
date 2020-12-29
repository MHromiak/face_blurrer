import cv2 



def draw_boxes(boxes, img):
    for box in boxes:
        x, y, w, h = box
        x2, y2 = x + w, y + h
        cv2.rectangle(img, (x,y), (x2, y2), (0,0,255), 1)



# Open the device at the ID 0

cap = cv2.VideoCapture(0)

#Check whether user selected camera is opened successfully.

if not (cap.isOpened()):
    print("Could not open video device")

#To set the resolution
cv2.namedWindow('preview', cv2.WINDOW_NORMAL)
cv2.resizeWindow('preview', 4320, 2880)

while(True):

    # Capture frame-by-frame

    ret, frame = cap.read()

    classifier = cv2.CascadeClassifier("haarcascade_pretrained.xml")

    bboxes = classifier.detectMultiScale(frame, 1.30, 7)


    # Display the resulting frame

    cv2.imshow('preview',frame)

    #Waits for a user input to quit the application

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture

cap.release()

cv2.destroyAllWindows()
