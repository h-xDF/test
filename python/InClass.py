
def add(parent,*heir):
    if len(heir) == 0:
        space[parent]
    else:
        space[parent] = heir




space = dict()
n = int(input())
for i in range(n):
    command = input().strip().split()
    buf = []
    if len(command) == 1:
        add(command[0],buf)
    else:
        for i in range(2,len(command),1):
            buf.append(command[i])
        add(command[0],buf)
