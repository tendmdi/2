count = 0
for x in range(500000, 550000):
  for y in range(18, (x//2+1)):
    if ((x % y) == 0) and ((y % 10) == 8):
      count+=1
      print(x,y)
      break
  if count == 5:
    break
