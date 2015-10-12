__author__ = 'Naveen Iyer (nki2kd)'


def maxmin(list):
    """returns the minimum and maximum of the list as a tuple"""
    tuple = ()
    listLength = len(list)
    if (listLength < 1):
        return None
    if (listLength == 1):
        return (list[0], list[0])
    min = list[0]
    max = list[0]
    for x in range(0, listLength):
        if (list[x] < min):
            min = list[x]
        if (list[x] > max):
            max = list[x]
    return (min, max)


def common_items(list1, list2):
    """returns the common items in list1 and list2 as a list"""
    commonItems = []
    for x in range(0, len(list1)):
        for y in range(0, len(list2)):
            if (list1[x] == list2[y]):
                a = True
                for z in range(0, len(commonItems)):
                    if (list1[x] == commonItems[z]):
                        a = False
                if (a == True):
                    commonItems.append(list1[x])
    return commonItems

def notcommon_items(list1, list2):
    """returns the items not in common between list1 and list2 as a list"""
    notCommonItems = []
    for x in list1:
        if not(x in list2):
            if not(x in notCommonItems):
                notCommonItems.append(x)
    for y in list2:
        if not(y in list1):
            if not(y in notCommonItems):
                notCommonItems.append(y)
    return notCommonItems

def count_list_items(list):
    """returns a dictionary of the values in the list, along with the number of times each value occurs"""
    count = {}
    for item in list:
        if (count.get(item) == 1):
            count[item] = count.get(item) + 1
        else:
            count[item] = 1

    return count


if __name__ == "__main__":
    A = [1, 3, 5, 7, 34 , 5 ,4 , 35445, 3]
    B = [1, 3, 54, 34, 34, 34, 34]

    C = [2,1]
    D = [5,1]

    E = ['A', 'B', 'E', 'Q','F','R', 'A']

    F = []

    print(maxmin(C))
    print(common_items(C,D))
    print(maxmin(A))
    print(common_items(A,B))
    print(maxmin(E))
    print(maxmin(F))
    print(notcommon_items(A,B))
    print(count_list_items(A))
    print(count_list_items(E))