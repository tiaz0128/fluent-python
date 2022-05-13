import struct
fmt = '<3s3sHH'
with open('cat.gif', 'rb') as fp:
  img = memoryview(fp.read())

header = img[:10]
print(bytes(header))
struct.unpack(fmt, header)

#$end
del header
del img
