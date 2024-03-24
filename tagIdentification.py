import pyscreeze
import re
from cnocr import CnOcr

from tag import *

tag = [0] * 6


def tagIdentify(click):
    tag1 = pyscreeze.screenshot(r"pic/tag1.jpg", region=(330, 352, 130, 43))
    tag2 = pyscreeze.screenshot(r"pic/tag2.jpg", region=(478, 352, 130, 43))
    tag3 = pyscreeze.screenshot(r"pic/tag3.jpg", region=(626, 352, 130, 43))
    tag4 = pyscreeze.screenshot(r"pic/tag4.jpg", region=(330, 417, 130, 43))
    tag5 = pyscreeze.screenshot(r"pic/tag5.jpg", region=(478, 417, 130, 43))
    tag6 = pyscreeze.screenshot(r"pic/tag6.jpg", region=(626, 417, 130, 43))

    ocr = CnOcr()
    text1 = ocr.ocr_for_single_line(r"pic/tag1.jpg")
    text2 = ocr.ocr_for_single_line(r"pic/tag2.jpg")
    text3 = ocr.ocr_for_single_line(r"pic/tag3.jpg")
    text4 = ocr.ocr_for_single_line(r"pic/tag4.jpg")
    text5 = ocr.ocr_for_single_line(r"pic/tag5.jpg")
    text6 = ocr.ocr_for_single_line(r"pic/tag6.jpg")

    t1 = text1['text']
    t2 = text2['text']
    t3 = text3['text']
    t4 = text4['text']
    t5 = text5['text']
    t6 = text6['text']

    tag[0] = re.sub('[·：’。.，“”、]', '', t1)
    tag[1] = re.sub('[·：’。.，“”、]', '', t2)
    tag[2] = re.sub('[·：’。.，“”、]', '', t3)
    tag[3] = re.sub('[·：’。.，“”、]', '', t4)
    tag[4] = re.sub('[·：’。.，“”、]', '', t5)
    tag[5] = re.sub('[·：’。.，“”、]', '', t6)

    print(tag)

    Six_Five_Stars(tag, click)
    if click[0] == -1:
        return click
    Five_Stars(tag, click)
    if click[0] == 1:
        return click
    Five_Four_Stars(tag, click)
    if click[0] == 1:
        return click
    Four_Five_Stars(tag, click)
    if click[0] == 1:
        return click
    Four_Stars(tag, click)
    if click[0] == 1:
        return click
    Four_Five_Stars(tag, click)
    if click[0] == 1:
        return click
    Four_Stars_1(tag, click)
    if click[0] == 1:
        return click
    Five_Stars_1(tag, click)
    if click[0] == 1:
        return click
    if click[0] == 0:
        return click
