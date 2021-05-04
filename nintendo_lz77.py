import struct

LZ10_MAGIC = 0x10
LZ11_MAGIC = 0x11

def read32(s):
    return struct.unpack('<L', s[:4])[0]

def lz10_uncompress(s: bytes):
    assert len(s) >= 4
    assert s[0x0] == LZ10_MAGIC
    
    pSrc = s[4:]
    pDest = bytearray(read32(s) >> 8)
    iSrc = 0
    iDest = 0
    while iDest < len(pDest): 
        uFlag = pSrc[iSrc]; iSrc += 1
        for i in range(8):
            if ((uFlag << i) & 0x80) == 0:
                pDest[iDest] = pSrc[iSrc]; iSrc += 1; iDest += 1
            else:
                nSize = ((pSrc[iSrc] >> 4) & 0x0F) + 3
                nOffset = (pSrc[iSrc] & 0x0F) << 8; iSrc += 1
                nOffset = (nOffset | pSrc[iSrc]) + 1; iSrc += 1
                iData = iDest - nOffset
                for j in range(nSize):
                    pDest[iDest] = pDest[iData + j]; iDest += 1
    return bytes(pDest)

def lz10_compress():
    pass

def lz11_uncompress():
    pass

def lz11_compress():
    pass