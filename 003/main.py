x = input("Podaj pierwszą liczbę: ")
y = input("Podaj drugą liczbę: ")
z = input("Podaj trzecią liczbę: ")

boki = [int(x),int(y),int(z)]

size = len(boki)

for i in range(size):
  for j in range(0, size-i-1):
    if boki[i] > boki[j+1]:
      boki[j], boki[j+1] = boki[j+1], boki[j]

if boki[0]+boki[1]>boki[2]:
  print("Z takich boków można zbudować trójkąt")

if boki[0]+boki[1]<boki[2]:
  print("Nie można zbudować trójkątu")

if boki[0]+boki[1]==boki[2]:
  print("Nie można zbudować trójkątu")
