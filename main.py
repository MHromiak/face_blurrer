from modify_img import *
from mtcnn.mtcnn import MTCNN 

import cv2
import sys




def live_video_blur():
    """ Uses the computer's live video feed to perform live face blurring.

        Excepts
        -------
        - Returns if no camera is found.

    """

    try:
        cap = cv2.VideoCapture(0)
    except:
        print("Could not find video camera")
        return

    cv2.namedWindow('face detection', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('face detection', 4096, 2880)
    front = cv2.CascadeClassifier('haarcascade_front.xml')
    profile = cv2.CascadeClassifier('haarcascade_profile.xml')

    _b = blur
    _a = attach

    while True:
        ret, frame = cap.read()
        boxes = []
        boxes_front = front.detectMultiScale(frame, 1.30, 1)
        boxes_profile = profile.detectMultiScale(frame, 1.30, 1)
        boxes.extend(boxes_front)
        boxes.extend(boxes_profile)

        if len(boxes) != 0:
            for box in boxes:
                x, y, w, h = box
                x2, y2 = x + w, y + h
                kW = int(w / 3.0)
                kH = int(h / 3.0)

                # ensure the width of the kernel is odd
                if kW % 2 == 0:
                    kW -= 1

                # ensure the height of the kernel is odd
                if kH % 2 == 0:
                    kH -= 1

                roi = (frame[y:y2, x:x2])
                blurred = _b(roi, (kW, kH))
                _a(blurred, frame, (x, x2), (y, y2))
            
            cv2.imshow('face detection',frame)

        #Waits for a user input to quit the application
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()


def video_blur(vid_path):
    """ Uses the computer's live video feed to perform live face blurring.

        Parameters
        ------
        vid_path : str
            Path to the video to be blurred (but not overwritten).

        Excepts
        -------
        - Returns if video  isn't found/cannot be opened.

    """

    try:
        cap = cv2.VideoCapture(vid_path)
    except:
        print("Could not find video at specified path/could not open video")
        return

    cv2.namedWindow('face detection', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('face detection', 4096, 2880)
    front = cv2.CascadeClassifier('haarcascade_front.xml')
    profile = cv2.CascadeClassifier('haarcascade_profile.xml')

    _b = blur
    _a = attach

    while True:
        ret, frame = cap.read()
        boxes = []
        boxes.extend(front.detectMultiScale(frame, 1.30, 1))
        boxes.extend(profile.detectMultiScale(frame, 1.30, 1))
        for box in boxes:
            x, y, w, h = box
            x2, y2 = x + w, y + h
            kW = int(w / 3.0)
            kH = int(h / 3.0)

            # ensure the width of the kernel is odd
            if kW % 2 == 0:
                kW -= 1

            # ensure the height of the kernel is odd
            if kH % 2 == 0:
                kH -= 1

            roi = (frame[y:y2, x:x2])
            blurred = _b(roi, (kW, kH))
            _a(blurred, frame, (x, x2), (y, y2))
        try:
            cv2.imshow('face detection',frame)
        except:
            print("Could not show image. Video may not be found")
            break
        #Waits for a user input to quit the application
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()


def img_blur(img_path):
    """ Blurs, but does not overwrite, an image.

        Parameters
        ------
        img_path : str
            Path to the image to be blurred (but not overwritten).

        Excepts
        -------
        - Returns if image  isn't found/cannot be opened.

    """
    try:
        pixels = cv2.imread(img_path)
    except:
        print("Could not find image at path " + img_path)
        return

    cv2.namedWindow('face detection', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('face detection', 4096, 2880)
    classifier = MTCNN()

    faces = classifier.detect_faces(pixels)

    _b = blur
    _a = attach

    draw_faces(faces, pixels)
    cv2.imshow('face detection', pixels)
    cv2.waitKey(0)
    pixels = cv2.imread(img_path)
    

    for face in faces:
        box = face['box']

        x, y, w, h = box
        x2, y2 = x + w, y + h
        kW = int(w / 3.0)
        kH = int(h / 3.0)

        # ensure the width of the kernel is odd
        if kW % 2 == 0:
            kW -= 1
        # ensure the height of the kernel is odd
        if kH % 2 == 0:
            kH -= 1

        roi = (pixels[y:y2, x:x2])
        blurred = _b(roi, (kW, kH))
        
        _a(blurred, pixels, (x, x2), (y, y2))
        
    cv2.imshow('face detection',pixels)

    cv2.waitKey(0)

    cv2.destroyAllWindows()


def help():
    print()
    print("-----------------------------------------------------------------------------")
    print("main.py - image, video, live video")
    print()
    print("Commands:")
    print()
    print("-h                       prints this info page")
    print("-video $path             begins blurring of video at path $path")
    print("-image $path             blurs image at path $path")
    print("no args                  connects to the computer's camera and blurs the live")
    print("                             stream")
    print("other inputs             prints this info page")




if __name__ == "__main__":

    if len(sys.argv) < 2:
        live_video_blur()

    if sys.argv[1].lower() == '-h':
        help()
        exit()
    elif sys.argv[1].lower() == '-video':
        vid = sys.argv[2]
        video_blur(vid)
    elif sys.argv[1].lower() == '-image':
        img = sys.argv[2]
        img_blur(img)
    else:
        ans = input("Command not recognized. Go to help page (Y/n)? ")
        if ans[0].lower() != 'n':
            help()
        exit()
