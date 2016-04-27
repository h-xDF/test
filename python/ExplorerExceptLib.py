# Если уже был добавин предок подаваемого исключения, то сообщить об этом 

space = dict()
Buf = set()
def add(heir,parent):
        # if len(parent) == 0:
        #     if heir in  space:
        #         return
        #     else:
        #         space[heir] = []
        # else:
        #     for i in parent:
        #         if i in space:
        #             space[i].append(heir)
        #         else:
        #             space[i] = [heir]
        #
        #
    space[heir] = []
    for i in parent:
        space[heir].append(i)

def explorer(target, list_parent):
    if len(list_parent) == 0:
        return False
    for i in space[list_parent]:
        if i in Buf:
            Buf.add(target)
            return True
    for i in space[list_parent]:
        if explorer(target,i):
            return True
        else:
            return False

def get(target):
    if target in Buf:
        return
    if len(Buf) == 0:
        Buf.add(target)
    else:
        if explorer(target,target):
            print(target)
        else:
            Buf.add(target)

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

m = int(input())
for i in range(m):
    get(input().strip())

add('A','B')
add('L',['D','F','G'])
add('M',[])
add('P',['A','L','M'])
get('B')
get('A')
    # def get(self,target):
    #     if
