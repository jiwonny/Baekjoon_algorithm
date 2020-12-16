N = int(input())
NUMBER = 666
count = 0
iter_num = 0

while count < N:
  iter_num += 1
  if str(NUMBER) in str(iter_num):
    count += 1
  
print(iter_num)
