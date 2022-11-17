x = input("Podaj pierwszą liczbę: ")
y = input("Podaj drugą liczbę: ")
z = input("Podaj trzecią liczbę: ")

boki = [int(x),int(y),int(z)]

bokis = sorted(boki)
print(bokis)

if bokis[0]+bokis[1]>bokis[2]:
  print("Z takich boków można zbudować trójkąt")

if bokis[0]+bokis[1]<bokis[2]:
  print("Nie można zbudować trójkątu")

if bokis[0]+bokis[1]==bokis[2]:
  print("Nie można zbudować trójkątu")
