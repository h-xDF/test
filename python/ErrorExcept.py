class test:
    def __init__(self):
        dict.__init__(self)

    def add(parent,heir):
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

    def get(target):
        
