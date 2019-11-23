import numpy as np
import cv2
from PIL import Image
import pytesseract
import re

def increase_range(bgr_uint8):
    flt = bgr_uint8.astype(np.float32) / 255.0
    flt = 3 * flt ** 2 - 2 * flt ** 3
    return (flt * 255).astype(np.uint8)


def extract_raw_text(path, blur):
    img = cv2.imread(path)
    height = img.shape[0]
    width = img.shape[1]
    img = cv2.resize(img, (900, int(900 * height/width)))

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img = cv2.GaussianBlur(img, (7, 7), blur)
    img = cv2.adaptiveThreshold(img, 125, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 12)

    #cv2.imshow("", img)
    #cv2.waitKey()

    s = pytesseract.image_to_string(img, lang="eng")
    for c in s:
        i = ord(c)
        if i > 255:
            print(i, c)
    ''',
                                    config="-c tessedit_char_whitelist=£.0123456789abcdefghijklmnopqrstuvwxyz"
                                    "ABCDEFGHIJKLMNOPQRSTUVWXYZ\\ ")'''
    return s


pattern = re.compile('.*\.[0-9][0-9]')

def extract_amount_lines(raw_text):
    return [line for line in raw_text.split("\n") if pattern.match(line)]

def clean_amount_lines(amout_lines):
    pass

s = extract_raw_text("test_data/test.jpg", 0.3)
lines = extract_amount_lines(s)

with open("out/out.txt", "w") as w:
    w.write("\n".join(lines))

s = extract_raw_text("test_data/tom.jpg", 0.3)
lines = extract_amount_lines(s)

with open("out/out2.txt", "w") as w:
    w.write("\n".join(lines))




