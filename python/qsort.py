# enter = [5,4,3,2,1,6]
#
# def sortnew(data,left,rght):

def psevdo_qsort(data):
    if data == []:
        return []
    else:
        #mid  = (data[0])
        pivot = data[0]
        left = psevdo_qsort([x for x in data[1:] if x < pivot])
        right = psevdo_qsort([x for x in data[1:] if x >= pivot])
        return left + [pivot] + right


enter = [-1,5,4,3,2,1,6,-1]
print(psevdo_qsort(enter))
