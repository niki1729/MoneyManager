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

if 4.0 == 4:
    print("yes")
