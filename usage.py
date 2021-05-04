from nintendo_lz77 import lz10_uncompress

with open('bin/test.lz77', 'rb') as f:
    s = f.read()

print('before:', s)
print('after:', lz10_uncompress(s))