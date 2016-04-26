
def add(heir,parent):
    if len(parent) == 0:
        if heir in  space:
            return
        else:
            space[heir] = []
    else:
        for i in parent:
            if i in space:
                space[i].append(heir)
            else:
                space[i] = [heir]


def get(parent,heir):
    if parent in space:
        if heir in space[parent]:
            return True
        else:
            for i in space[parent]:
                if get(i,heir):
                    return True
    else:
        return


def explorer(parent,heir):
    if parent == heir:
        print('Yes')
        return

    if get(parent,heir):
        print('Yes')
        #return True
    else:
        print('No')
        #return False




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

q = int(input())
for i in range(q):
    command = input().strip().split()
    explorer(command[0],command[1])

### test_suite

add('classA',['classB','classC','classD','classG','classH'])
add('classB',['classC','classE','classG','classH','classK','classL'])
add('classC',['classE','classD','classH','classK','classL'])
add('classE',['classD','classF','classK','classL'])
add('classD',['classG','classH'])
add('classF',['classK'])
add('classG',['classF'])
add('classH',['classL'])
add('classK',['classH','classL'])
add('classL',[])


if __name__ == '__main__':
    assert explorer('classK','classD') == True, "1"
    assert explorer('classD','classA') == True, "2"
    assert explorer('classG','classD') == True, "3"
    assert explorer('classH','classA') == True, "4"
    assert explorer('classE','classE') == True, "5"
    assert explorer('classH','classG') == True, "6"
    assert explorer('classE','classL') == False, "7"
    assert explorer('classB','classD') == False, "8"
    assert explorer('classD','classL') == False, "9"
    assert explorer('classD','classG') == False, "10"
    assert explorer('classD','classE') == True, "11"
    assert explorer('classA','classF') == False, "12"
    assert explorer('classA','classC') == False, "13"
    assert explorer('classK','classA') == True, "14"
    assert explorer('classA','classH') == False, "15"
    assert explorer('classK','classD') == True, "16"
    assert explorer('classH','classB') == True, "17"
    assert explorer('classK','classB') == True, "18"
    assert explorer('classD','classL') == False, "19"
    assert explorer('classG','classG') == True, "20"
    assert explorer('classA','classH') == False, "21"
    assert explorer('classK','classL') == False, "22"
    assert explorer('classG','classE') == True, "23"
    assert explorer('classB','classA') == True, "24"
    assert explorer('classC','classK') == False, "25"
    assert explorer('classK','classL') == False, "26"
    assert explorer('classC','classL') == False, "27"
    assert explorer('classG','classC') == True, "28"
    assert explorer('classD','classD') == True, "29"
    assert explorer('classC','classG') == False, "30"
    assert explorer('classE','classA') == True, "31"
    assert explorer('classF','classK') == False,"32"
    assert explorer('classB','classG') == False, "33"
    assert explorer('classH','classL') == False, "34"
    assert explorer('classL','classF') == True, "35"
    assert explorer('classH','classG') == True, "36"
    assert explorer('classD','classA') == True, "37"
    assert explorer('classH','classL') == False, "38"
