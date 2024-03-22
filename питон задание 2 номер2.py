x=5**36+5**24-25
count=0
while x>0:
    if x%5==4:
        count+=1
    x//=5
print(count)
