
# head_b = "# coding: euc_kr\n".encode(encoding='euc_kr')

f = open('4-8.txt', encoding='utf_8')
a = f.readline()
code_b = str(a).encode(encoding='euc_kr')

f2 = open("4-8.not-anno.py", 'wb')

# f2.write(head_b)
f2.write(code_b)