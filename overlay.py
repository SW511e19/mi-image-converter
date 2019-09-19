#!/usr/bin/env python3
import sys
import os
from PIL import Image

def main(argv=[__name__]):

    logo = "black.png"
    outimage = "test.png"
    path = "images"

    for filename in os.listdir(path):
        if (filename.endswith('.jpg') or filename.endswith('.png')):
            inimage = filename
            add_logo(path + "/" + inimage, logo, filename)
    return 0


def add_logo(mfname, lfname, outfname):

    mimage = Image.open(mfname)
    limage = Image.open(lfname)

    # resize logo
    wsize = int(min(mimage.size[0], mimage.size[1]) * 1)
    wpercent = (wsize / float(limage.size[0]))
    hsize = int((float(limage.size[1]) * float(wpercent)))

    simage = limage.resize((wsize, hsize))
    mbox = mimage.getbbox()
    sbox = simage.getbbox()

    # right bottom corner
    box = (mbox[2] - sbox[2], mbox[3] - sbox[3])
    mimage.paste(simage, box, mask=simage)
    mimage.save(outfname)


if __name__ == "__main__":
    sys.exit(main(sys.argv))