import sys

sys.set_int_max_str_digits(2147483647)

import os

import matplotlib.pyplot as plt
import io
import base64

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

prime_array = []
multiple_of_2_DIVIDE_multiple_of_4_array = []

for i in range(5, param):
  if (isPrime(i) == True):
    prime_array.append(i)
    if (len(str(i)) < 15):
      if ((i - 1)%4 == 0):
        multiple_of_4 = multiple_of_4 + 1
      else:
        multiple_of_2 = multiple_of_2 + 1
    else:
      if (int(str(i - 1)[len(str(i - 1)) - 2: len(str(i - 1))])%4 == 0):
        multiple_of_4 = multiple_of_4 + 1
      else:
        multiple_of_2 = multiple_of_2 + 1
    multiple_of_2_DIVIDE_multiple_of_4_array.append(multiple_of_2/multiple_of_4)

print(f"multiple_of_2: {multiple_of_2}")
print(f"multiple_of_4: {multiple_of_4}")
print(f"multiple_of_2 - multiple_of_4: {multiple_of_2 - multiple_of_4}")
print(f"multiple_of_2 / multiple_of_4: {multiple_of_2 / multiple_of_4}")

plt.plot(prime_array, multiple_of_2_DIVIDE_multiple_of_4_array)
plt.xlabel('Prime Number')  
plt.ylabel('multiple_of_2 / multiple_of_4')
plt.title(f'multiple_of_2 / multiple_of_4 ( 5 ~ {param} (Only Prime Number) )')

buffer = io.BytesIO()
plt.savefig(buffer, format='png')
buffer.seek(0)
img_base64 = base64.b64encode(buffer.read()).decode('utf-8')
img_url = f"data:image/png;base64,{img_base64}"

print("==============================================================================================================================")
print(img_url)
print("==============================================================================================================================")
os.system(f'echo "<code>{img_url}</code>" >> $GITHUB_STEP_SUMMARY')
