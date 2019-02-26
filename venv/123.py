a = ""
with open('file.txt') as f:
   a = f.readline().strip()
itog = ''
bufer_bukv = ''
bufer_cifr = ''
count = 0
count1 = 0
asd = a[count]
while count < len(a):
    if not a[count].isdigit():
        bufer_bukv += a[count]
        count += 1
    if a[count].isdigit():
        bufer_cifr += a[count]
        if count != len(a):
            count += 1
        if count == len(a):
            itog += bufer_bukv * int(bufer_cifr)
            with open('file1.txt', 'w') as b:
                b.write(itog)
                break
        if not a[count].isdigit():
            itog += bufer_bukv * int(bufer_cifr)
            bufer_cifr = ''
            bufer_bukv = ''
            count1 = 0
