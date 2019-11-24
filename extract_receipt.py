import numpy as np
import cv2
from PIL import Image
import pytesseract
import re


def increase_range(bgr_uint8):
    flt = bgr_uint8.astype(np.float32) / 255.0
    cube = 3 * flt ** 2 - 2 * flt ** 3
    flt = flt * 0.8 + cube * 0.2
    return (flt * 255).astype(np.uint8)


def extract_raw_text(file, blur):
    byte = file.read()

    img = cv2.imdecode(np.fromstring(byte, dtype=np.uint8), flags=cv2.IMREAD_COLOR)
    height = img.shape[0]
    width = img.shape[1]
    img = cv2.resize(img, (900, int(900 * height / width)))

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img = increase_range(img)
    img = cv2.GaussianBlur(img, (7, 7), blur)
    img = cv2.adaptiveThreshold(img, 125, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 12)

    # cv2.imshow("", cv2.resize(img, (600, 900)))
    # cv2.waitKey()

    s = pytesseract.image_to_string(img, lang="eng")
    # for c in s:
    #     i = ord(c)
    #     if i > 255:
    #         print(i, c)
    ''',
                                    config="-c tessedit_char_whitelist=£.0123456789abcdefghijklmnopqrstuvwxyz"
                                    "ABCDEFGHIJKLMNOPQRSTUVWXYZ\\ ")'''
    return s


pattern = re.compile('.*([0-9]*\.[0-9][0-9])')
number_pattern = re.compile("(.*?)( ?£?)([0-9]+\.[0-9][0-9])")

def extract_amount_lines(raw_text):
    return [line for line in raw_text.split("\n") if pattern.match(line)]


def checksum(amount_list, total):
    return sum(amount_list) == total


def clean_line(line):
    # find idx of .
    if not pattern.match(line):
        print("what")
    matched = number_pattern.match(line)
    item = matched.group(1)
    price = int(100 * float(matched.group(3)))
    return item, price


def clean_amount_lines(amount_lines):
    amount_list = []
    item_list = []
    for line in amount_lines:
        if "TOT" in line.upper():  # end of list
            break
        else:
            item, amount = clean_line(line)
            item_list.append(item)
            amount_list.append(amount)

    return item_list, amount_list

def process_file(file):
    s = extract_raw_text(file, 0.3)
    lines = extract_amount_lines(s)
    items, prices = clean_amount_lines(lines)

    with open("out/0.jpg", "w") as w:
        w.write("\n".join(items))
        w.write("\n".join([str(p) for p in prices]))


# process_file(open("test_data/test.jpg", "rb"))