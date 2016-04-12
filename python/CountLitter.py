
# через while сделать чтение из файла и контенизацию прочитанных строк
#
S = str("as de fr De ED FR qweer")
output = open('CountLitter.txt', 'w')
l = list(S.lower().split())
s = set(l)
d = {}
d = d.fromkeys(s)
for i in range(len(l)):
    if type(d[l[i]]) != int:
        d[l[i]] = int(1)
    else:
        d[l[i]] += 1
Buf = int(0)
for key in d.keys():
    if d[key] > Buf:
        Buf = d[key]
# for value in
# output.write()
print(d)
for key in d.keys():
    if d[key] == Buf:
        output.write(str(key) + " " + str(Buf) + " ")

output.close()
# for value in d.values():
#     if value == Buf: print(value)

# print(d)
# print()
# print(Buf)
