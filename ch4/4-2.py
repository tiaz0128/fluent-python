#4-2

py_bytes = bytes('파이썬', encoding='utf_8')
print(py_bytes[0])
print(py_bytes[:1]) 

py_arr = bytearray(py_bytes)
print(py_arr)
print(py_arr[-1:])