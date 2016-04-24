# create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри пространства <parent>
# add <namespace> <var> – добавить в пространство <namespace> переменную <var>
# get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var> при запросе из пространства <namespace>, или None, если такого пространства не существует



space =  {'global' : {'vars' : [], 'parent' : None}}
def create(namespace,parent):
    space.update({namespace : {'vars' : [], 'parent' : parent}})
def add(namespace,var):
    space[namespace]['vars'].append(var)
def get(namespace,var):
    flag = bool(False)
    for i in range(len(space[namespace]['vars'])): # смотрим в своём найм-спйсе
        if space[namespace]['vars'][i] == var:
            print(namespace)
            flag = True
            break
    if flag == True:
         return
    else:
        if space[namespace]['parent'] == None:
            print(None)
        else:
            get(space[namespace]['parent'], var) # вызываем тот найм спйс к которому сами пренадлежим


n = int(input())
for i in range(n):
    command = input().split()
    if command[0] == 'add':
        add(command[1],command[2])
    if command[0] == 'create':
        create(command[1],command[2])
    if command[0] == 'get':
        get(command[1],command[2])

#test_date
# create('test1','global')
# add('global',2)
# get('test1',2)
