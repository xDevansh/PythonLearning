print("Module is imported")

def find_index(list,target):
    for idx,i in enumerate(list):
        if i==target:
            return idx
    return -1
