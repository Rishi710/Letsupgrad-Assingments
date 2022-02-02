# Take multiple numbers as input and print the sum
# 10 20 30 40 50
x = [int(i) for i in input('Enter integer values: ').split()]

s = 0;
for j in x:
  s += j # sum = sum + j;

print(s);