import struct
import binhex
def strTrans(argv):
    rec = argv.split()
    sume = ''
    for bhex  in rec:
        cb = int(bhex,16)
        cb = struct.pack('i'.cb)
        cb = cb[:1]
        sume += cb
    print(sume)
    checksum=b
