#!/usr/bin/env python2

import sys
import os
from PIL import Image

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage: %s [image name]" % (sys.argv[0],)
        sys.exit(-1)

    im = Image.open(sys.argv[1])
    pix = im.load()

    filename = os.path.splitext(sys.argv[1])[0]
    f = open(filename + ".h", "w+")
    f.write("#include <stdint.h>\n\n");
    f.write("static const uint32_t %s_WIDTH=%d;\n" % (filename.upper(), im.size[0]))
    f.write("static const uint32_t %s_HEIGHT=%d;\n" % (filename.upper(), im.size[1]))
    f.write("static const uint8_t %s_DATA[]={" % (filename.upper()))


    for y in xrange(0, im.size[1]):
        for x in xrange(0, im.size[0]):
            r, g, b, a = pix[x, y]
            f.write("%s, " % hex(r))
            f.write("%s, " % hex(g))
            f.write("%s, " % hex(b))
            f.write("%s, " % hex(a))

    f.write("};\n")
    f.close()

