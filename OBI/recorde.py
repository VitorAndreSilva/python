L = int(input())
M = int(input())
R = int(input())

if L>R and L>M:
  print("*")
  print("*")
elif L<M:
  print("RM")
  print("RO")
elif L<R and L>M:
  print("*")
  print("RO")
else:
  print("*")
  print("*")