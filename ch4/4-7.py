# 4-7

octets = b'Montr\xe9al'

octets.decode('cp1252')

octets.decode('iso8859_7')

octets.decode('koi8_r')

print(octets.decode('utf_8', errors='replace'))
