import sys
import os

sys.set_int_max_str_digits(2147483647)

param = int(sys.argv[1])

# 짝수인 자연수만 연산 가능
def dividing_2(n):
  if (len(str(n)) < 16):
    return n//2
  return int(str((n * 5))[0:len(str(n * 5)) - 1])

# 3 이상의 자연수만 소수 판별 가능 
def isPrime(n):
  if (int(str(n)[-1])%2 == 1):
    for i in range(2, dividing_2(n + 1)):
      if n % i == 0:
        return False
    return True
  else:
    return False

multiple_of_2 = 0
multiple_of_4 = 0

for i in range(3, param):
  if (isPrime(i) == True):
    if (len(str(i)) < 15):
      if (i%4 == 0):
        multiple_of_4 = multiple_of_4 + 1
      else:
        multiple_of_2 = multiple_of_2 + 1
    else:
      if (int(str(i)[len(str(i)) - 2: len(str(i))])%4 == 0):
        multiple_of_4 = multiple_of_4 + 1
      else:
        multiple_of_2 = multiple_of_2 + 1

print(f"multiple_of_2: {multiple_of_2}")
print(f"multiple_of_4: {multiple_of_4}")
print(f"multiple_of_2 - multiple_of_4: {multiple_of_2 - multiple_of_4}")
