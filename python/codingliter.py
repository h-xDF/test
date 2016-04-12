import re

intput = open('test.txt', 'r')
output = open('oput.txt', 'w')

astr = intput.readline()

intput.close()

primerD = {'0','1','2','3','4','5','6','7','8','9'}
Buf = str()
amount = int(0)
j = int(0)

while j < (len(astr) - 1):
    amount = int(j + 1)
    BufInt = str()
    while astr[amount] in primerD:
        BufInt = BufInt + astr[amount]
        if amount >= (len(astr) - 1): break
        amount += 1
    # print(type(BufInt))
    # print(BufInt)
    # print()
    for i in range(int(BufInt)):
        Buf = Buf + astr[j]
        i += 1
    j = amount

# print(astr[1])
# print(type(int(astr[1])))

Buf = Buf + "\n"
output.write(Buf)

output.close()
#
#
# S = {0,1,2,3,4,5,6,7,8,9}
# p = int(2)
# res = p in S
# print(res)
