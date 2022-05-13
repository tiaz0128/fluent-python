# 4-5

for codec in ['euc_kr', 'utf_8', 'utf_16']: #latin_1
  print(codec, '파이 썬'.encode(codec), sep='\t')