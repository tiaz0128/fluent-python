# 4-6

city = '서울'

city.encode('utf_8')

city.encode('utf_16')

city.encode('euc_kr')

#에러 발생
print(city.encode('cp437', errors='replace'))