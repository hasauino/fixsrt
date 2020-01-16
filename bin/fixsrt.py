#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 20:50:22 2020
@author: Hassan Umari
"""

from pysrt.srtitem import SubRipItem
from pysrt.srtfile import SubRipFile 
import pysrt
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=
                                                "covert a .srt exported file \
                                                from sonix.ai which has coded \
                                                double lines to a normal srt \
                                                file. \
                                                Ex:\
                                                fixsrt myFile.srt --output convertedFile.srt")
    parser.add_argument('file', type=str, help="file to be converted")
    parser.add_argument('--output', type=str, default="output",
                 help="name of output file without extention (default: output)")

    parser.add_argument('--eol', type=str, default="###",
                 help="End of line marker (default: ###)")
    
    args=parser.parse_args()

    subs = pysrt.open(args.file)
    after_subs = []

    indx = 1
    iterator = iter(subs)

    while True:
        try:
            sub = next(iterator)
        except StopIteration:
            break

        if sub.text[-len(args.eol):] != args.eol:
            after_subs.append(SubRipItem(indx, sub.start, sub.end, sub.text))
        else:
            line2_sub = next(iterator)
            text = sub.text[:-len(args.eol)] + '\n' + line2_sub.text
            combined_sub = SubRipItem(indx, sub.start, line2_sub.end, text=text)
            after_subs.append(combined_sub)
        indx += 1

    after = SubRipFile(items=after_subs)
    after.save(args.output + '.srt', encoding='utf-8')
