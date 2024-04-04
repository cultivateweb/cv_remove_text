import cv2
import easyocr
import math

import numpy as np

from PIL import Image


def midpoint(x1: int, y1: int, x2: int, y2: int) -> tuple:
    """
    The start point will be the mid-point between the top-left corner and
    the bottom-left corner of the box.
    the end point will be the mid-point between the top-right corner and the bottom-right corner.

    :param x1:
    :param y1:
    :param x2:
    :param y2:
    :return:
    """
    x_mid = int((x1 + x2)/2)
    y_mid = int((y1 + y2)/2)
    return x_mid, y_mid


def cv_remove_text(file_from: str, file_to: str) -> None:
    """
    Remove text from image

    :param file_from:
    :param file_to:
    :return:
    """
    print(file_from, file_to, sep=" -> ")
    pil_img = Image.open(file_from)
    image = np.asarray(pil_img)
    inpainted_img = img = image
    mask = np.zeros(img.shape[:2], dtype="uint8")
    reader = easyocr.Reader(['ru', 'en'])
    result = reader.readtext(pil_img)
    print(result)
    for item in result:
        box, _, _ = item
        x0, y0 = box[0]
        x1, y1 = box[1]
        x2, y2 = box[2]
        x3, y3 = box[3]
        x_mid0, y_mid0 = midpoint(x1, y1, x2, y2)
        x_mid1, y_mi1 = midpoint(x0, y0, x3, y3)
        thickness = int(math.sqrt( (x2 - x1)**2 + (y2 - y1)**2))
        cv2.line(mask, (x_mid0, y_mid0), (x_mid1, y_mi1), 255, thickness)
        inpainted_img = cv2.inpaint(img, mask, 7, cv2.INPAINT_NS)

    cv2.imwrite(file_to, cv2.cvtColor(inpainted_img, cv2.COLOR_BGR2RGB))
