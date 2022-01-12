﻿import fitz
from paddleocr import PaddleOCR
# from paddleocr import PPStructure
import logging
import sys
import cv2
import numpy as np


logger = logging.getLogger()
pOCR = PaddleOCR(type='STRUCTURE',lang='ch')
# pStru = PPStructure(type='STRUCTURE',lang='ch')
mat = fitz.Matrix(4.0, 4.0)

def pdf_ocr(url):
    print(url)
    try:
        doc = fitz.open(url)
    except Exception as E:
        logger.error(E)

    out_url = '/'.join(url.split("/")[:-1]) + "/" + '.'.join(url.split("/")[-1].split(".")[:-1]) + '_ocr.md'
    with open(out_url, 'a') as f:
        for page in doc:
            pix = page.get_pixmap(
            colorspace=fitz.csGRAY,
            matrix=mat)
        #    clip=bbox)
            image = pix.tobytes("png")
            print(type(image))

            np_arr = np.frombuffer(image, dtype=np.uint8)
            img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
            rst = pOCR(img)
            # rst = pStru(img)
            for e in rst[1]:
                f.write(e[0])
            f.write("\n\t\t\t\t第 %i 页\n" % page.number+1)
        f.close()






if __name__ == "__main__":
    if 
    url = "I:/Misc/CV/SapE.pdf"
    pdf_ocr(url)
