#4-1

s = '파이썬'
print(len(s))

b = s.encode('utf16-le')
print(b)
print(len(b))

c = b.decode('utf8')
print(c)
print(len(c))
