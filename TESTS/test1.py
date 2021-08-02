"""print([400, '29.07.21', '18:55:16', 'shoes', 'clothes', '2907211855163735359'])
l = "[400, '29.07.21', '18:55:16', 'shoes', 'clothes', '2907211855163735359']"


# l = list(l)
# print(l)
# print(l[4])


def parser_string_to_transaction_item(liste):
    print("LISTE:" + str(liste))
    result = []
    index = 1  # we directly skipp [

    amount = []
    date = []
    time_trans = []
    name = []
    category = []
    id = []
    print(liste[index])

    while liste[index] != ",":
        if liste[index] != "'" and liste[index] != " ":
            amount.append(liste[index])
        index += 1
    result.append("".join(amount))
    print(result)
    index +=2
    while liste[index] != ",":
        if liste[index] != "'" and liste[index] != " ":
            date.append(liste[index])
        index += 1
    result.append("".join(date))
    print(result)
    index +=2
    while liste[index] != ",":
        if liste[index] != "'" and liste[index] != " ":
            time_trans.append(liste[index])
        index += 1
    result.append("".join(time_trans))
    print(result)
    index +=2
    while liste[index] != ",":
        if liste[index] != "'" and liste[index] != " ":
            name.append(liste[index])
        index += 1
    print(result)
    result.append("".join(name))
    index +=2
    while liste[index] != ",":
        if liste[index] != "'" and liste[index] != " ":
            category.append(liste[index])
        index += 1
    print(result)
    result.append("".join(category))
    index +=2
    while liste[index] != ",":
        if liste[index] != "'" and liste[index] != " ":
            id.append(liste[index])
        index += 1
    print(result)
    result.append("".join(id))
    print(result)
    return result


# print(parser_string_to_transaction_item(l))

def parser_string_to_transaction_item1(liste):
    print("LISTE:" + str(liste))
    print(liste[10])
    result = []
    index = 1  # we directly skipp [

    amount = []
    date = []
    time_trans = []
    name = []
    category = []
    id = []
    print(liste[index])

    while liste[index] != ",":
        if liste[index] != " " and liste[index] != "'":
            amount.append(liste[index])
        index += 1
    print(amount, liste[index])
    result.append("".join(amount))
    index +=2

    while liste[index] != ",":
        if liste[index] != " " and liste[index] != "'":
            date.append(liste[index])
        index += 1
    print(date, liste[index])
    result.append("".join(date))
    index += 2

    while liste[index] != ",":
        if liste[index] != " " and liste[index] != "'":
            time_trans.append(liste[index])
        index += 1
    print(time_trans, liste[index])
    result.append("".join(time_trans))
    index += 2

    while liste[index] != ",":
        if liste[index] != " " and liste[index] != "'":
            name.append(liste[index])
        index += 1
    print(name, liste[index])
    result.append("".join(name))
    index += 2

    while liste[index] != ",":
        if liste[index] != " " and liste[index] != "'":
            category.append(liste[index])
        index += 1
    print(category, liste[index])
    result.append("".join(category))
    index += 2

    while liste[index] != "]":
        if liste[index] != " " and liste[index] != "'":
            id.append(liste[index])
        index += 1
    print(id, liste[index])
    result.append("".join(id))
    return str(result)


print("result:" + parser_string_to_transaction_item1(l))
"""
"""l=["1", "2", "3"]
l.pop(2)
# l.remove("2")
print(l)"""

"""l=[['200', '30.07.21', '08:32:26', 'name2', 'car', '3007210832267783645'], ['300', '30.07.21', '08:32:26', 'name3', 'car', '3007210832268081910']]
print(l[1][0])
l[1][0]=280
print(l)"""

"""if 4.0 == 4:
    print("yes")"""
"""
liste = [[1], [2], [3], [5]]


def change_two_categories_by_prio(list, ind1, ind2):
    interm = list[ind1][0]
    list[ind1][0] = list[ind2][0]
    list[ind2][0] = interm

"""
"""
def enter_after_prio(list, element):
    I have now 3 ifs (2 ifs and else) i think this can reduce execution time in some rare casses.
    Need to ask
    !!!ADD TO DO!!!!
    :param list:
    :param element: what we need to rearrange
    :return: new arranged list
    if element[0] > list[lowest_priority(list)][0]:
        list.append(element)
        return list
    print(highest_priority(list))
    if element[0] < list[highest_priority(list)][0]:
        result = []
        result.append(element)
        for i in list:
            i[0] = i[0] + 1
            result.append(i)
        return result

    else:
        ind=0
        result=[]
        while element[0]< list[ind][0]:
            if element
            result.append(list[ind])
            ind +=1
        result.append(element)
        for i in range(len(list)-ind):
            pass
"""
"""
def highest_priority(list):

    :return gives the index from list back of the highest priority account
    
    high_prio = list[0][0]
    index = 0
    for i in range(len(list)):
        if list[i][0] < high_prio:
            index = i
    print(index, "index")
    return index


def lowest_priority(list):
    
    :return gives the index from self.list_accounts back of the lowest priority account
    
    lowest_prio = list[0][0]
    index = 0
    for i in range(len(list)):
        if list[i][0] > lowest_prio:
            index = i
    return index


# print(liste[lowest_priority(liste)][0])
# liste = enter_after_prio(liste, [0])
print(liste)
"""


def enter_after_prio(liste, index, prio):
    """
    :param list: will be later self
    :param index: of the element that is already in the list but needs to change priority drastically
    :param prio: the new prio
    :return:
    """
    element = liste[index]
    liste.pop(index)  # pop with index
    if prio > liste[lowest_priority(liste)][0]:
        liste.append(element)
        return liste
    print(prio, highest_priority(liste), "double", )
    if prio < liste[highest_priority(liste)][0]:

        result = []
        result.append(element)
        for i in liste:
            result.append(i)
        liste = result
        print(result)
        return liste

    else:
        ind = 0
        result = []
        while liste[ind][0] <= prio:
            result.append(liste[ind])
            ind += 1
        result.append(element)

        for i in range(len(liste) - ind):
            result.append(liste[i + ind])
        return result


def highest_priority(liste):
    high_prio = liste[0][0]
    index = 0
    for i in range(len(liste)):
        if liste[i][0] < high_prio:
            index = i
            high_prio = liste[i][0]
    print(high_prio)
    print(index, "index")
    return index


def lowest_priority(liste):
    lowest_prio = liste[0][0]
    index = 0
    for i in range(len(liste)):
        if liste[i][0] > lowest_prio:
            index = i
            lowest_prio = liste[i][0]
    return index


liste = [[1, "1"], [2, "2"], [3, "3"], [5, "5"]]

liste = enter_after_prio(liste, 1, 3)
print(liste)
