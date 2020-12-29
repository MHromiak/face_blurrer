import cv2
from typing import Tuple, List


def draw_boxes(boxes : List[list], img):
    """ Draws bounding boxes around the regions of interest (ROIs) in 'boxes' onto image 'img'

        Overwrites 'img', but does not overwrite the source file.

        Parameters
        ----------
        boxes : List[list]
            The x, y, width and height of the bounding box to be drawn. If box cannot be drawn,
              a warning message is printed to stdout.
            
        img : numpy.ndarray
            Array representation of an image to be drawn to.

    """

    for box in boxes:
        x, y, w, h = box
        x2, y2 = x + w, y + h

        try:
            cv2.rectangle(img, (x,y), (x2, y2), (0,0,255), 1)
        except:
            print("Could not draw box " + str(box) +  " on image")


def draw_faces(faces, img):
    """ Draws eye points, nose and smile points and bounding boxes around the regions of interest (ROIs) 
            in 'boxes' onto image 'img'

        Overwrites 'img', but does not overwrite the source file.

        Used with the MTCNN() model from the package from 'mtcnn.mtcnn'.

        Parameters
        ----------
        faces : dict
            A dictionary of the bounding box and keypoints described above. If box or point cannot be drawn,
              a warning message is printed to stdout.
            
        img : numpy.ndarray
            Array representation of an image to be drawn to.

    """
    for face in faces:
        x, y, w, h = face['box']
        x2, y2 = x + w, y + h
        try:
            cv2.rectangle(img, (x,y), (x2, y2), (0,0,255), 1)
        except:
            print("Could not draw box " + str(face['box']) +  " on image")

        for point in face['keypoints'].values():
            try:
                cv2.circle(img, point, 1, (0, 0, 255), cv2.FILLED)
            except:
                print("Could not draw point " + str(point) +  " on image")
            

def blur(roi, k):
    """ Performs a gaussian blur on a region of interest

        Parameters
        ----------
        roi : numpy.ndarray
            Array representation of an image to be blurred.
            
        k : Tuple(int)
            Gaussian kernel dimensions.
        
        
        Returns
        -------
        Blurred version of roi.
            
    """
    return cv2.GaussianBlur(roi, k, 0)


def attach(blurred, img, xs : Tuple[int], ys : Tuple[int]):
    """ Overwrites a region of interest onto an image using the coordinate tuples xs, ys

        Parameters
        ----------
        blurred : numpy.ndarray
            Array representation of an image to be attached.

        img : numpy.ndarray
            Array representation of an image to be attached to.
            
        xs : Tuple(int)
            x coordinates representing the ends of where blurred should be attached to on img.

        ys : Tuple(int)
            y coordinates representing the ends of where blurred should be attached to on img.     
    """
    img[ys[0]:ys[1], xs[0]:xs[1]] = blurred