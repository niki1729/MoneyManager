import time
from random import randint

list_transaction = open("backend/usr_data/list_transactions.txt", "a")
list_transaction.close()


def init_example():
    list_transaction = open("backend/usr_data/list_transactions.txt", "w")
    n = ['rent', 'insurance', 'car', 'eat', 'clothes']
    for i in range(5):
        list_transaction.write(
            str([i * 100, str(time.strftime('%d.%m.%y')), str(time.strftime("%H:%M:%S")), 'name' + str(i), n[i],
                 '{0}{1}{2}'.format(str(time.strftime('%d%m%y')),
                                    str(time.strftime('%H%M%S')), str(randint(1000000, 9999999)))]) + "\n")
    list_transaction.close()


class TransactionListControl:
    """
    Class that can save the list (with the transaction items),
    add, delete transactions and find the entries you need (by index and the word). It can also display
    the total amount of money, spend and the difference.
    !
    !
    !
    need on function that can tell the highest priority and rearrange priorities
    and need one function that will control if the data in the input is correct
    !
    !
    !
    ALSO FOR THE OTHER TYPES!: TRANSACTIONS AND CATEGORIES
    """

    def __init__(self):
        self.transaction_list_work = []
        list_transaction = open("backend/usr_data/list_transactions.txt", "r")
        for i in list_transaction:
            self.transaction_list_work.append(self.parser_string_to_transaction_item1(i[:-1]))
        list_transaction.close()
        # print(self.get_len_list_transaction())    works
        # print(self.transaction_list_work[5][2])

    def add_transaction(self, amount, date, time_trans, name, category, account):
        self.transaction_list_work.append([amount, date, time_trans, name, category, account,
                                           "{0}{1}{2}".format(str(time.strftime("%d%m%y")),
                                                              str(time.strftime("%H%M%S")),
                                                              str(randint(1000000000, 9999999999)))])
        # the last one is the id, created with date and time when created and random number (nearly unique)
        # print(self.transaction_list_work)

    def delete_transaction_by_index(self, index):
        """
        :param index: deletes a transaction item by the index of the transaction_list_work NOT by the ID
        """
        self.transaction_list_work.pop(index)  # pop with index

    def save_listtransaction_to_file(self):
        len_txt_file = self.get_len_list_transaction()
        len_transaction_list_work = len(self.transaction_list_work)

        list_transaction = open("usr_data/list_transactions.txt", "w")
        diff = len_transaction_list_work - len_txt_file
        print("diff" + str(diff))
        if diff <= 0:
            for i in self.transaction_list_work:
                list_transaction.write(str(i) + "\n")
        else:
            for i in self.transaction_list_work:
                list_transaction.write(str(i) + "\n")
            for i in range(diff):
                list_transaction.write("")
        list_transaction.close()

    def find_after_ind_and_criteria(self, index, criteria):
        """
        :param index: is the index from the list (so 0 for costs till 5 id)
        :param criteria: what is asked more precisely
        :return:
        """
        result = []
        for i in self.transaction_list_work:
            # print(i)
            if i[index] == criteria:
                # print(i)
                result.append(i)
        return result

    def change_transaction(self, index, id, old_info, new_info):
        """
        :param index: is the index from the list (so 0 for costs till 5 id)
        :param id: with id it would be easier to search
        :param old_info: not necessary if id is known
        :param new_info: with what the thing needs to change
        """
        if id != "":
            try:
                for i in range(len(self.transaction_list_work)):
                    if int(self.transaction_list_work[i][5]) == int(id):
                        self.transaction_list_work[i][index] = new_info
            except:
                return "HI"

    def total_sum(self):
        """
        :return: total positif for all transactions and also total negative and the difference
        """
        result_pos = 0
        result_neg = 0
        result_diff = 0
        for i in self.transaction_list_work:
            amount = int(i[0])
            if amount >= 0:
                result_pos += amount
            if amount < 0:
                result_neg += amount
        result_diff = result_pos + result_neg
        return result_pos, result_neg, result_diff

    @staticmethod
    def get_len_list_transaction():
        """
        :return: the lenght of the list_transaction.txt
        """
        file = open("usr_data/list_transactions.txt", "r")
        index = 0
        mot = "a"
        while mot != '':
            mot = file.readline()
            index = index + 1
        file.close()
        return int(index - 1)

    @staticmethod
    def parser_string_to_transaction_item1(liste):
        """
        :param liste: is the transaction item, that is a string in the .txt file so needs to be parsed
        :return: list with the transaction item not a string list
        """
        result = []
        index = 1  # we directly skipp [

        amount = []
        date = []
        time_trans = []
        name = []
        category = []
        account = []
        id = []

        while liste[index] != ",":
            if liste[index] != " " and liste[index] != "'":
                amount.append(liste[index])
            index += 1

        index += 2

        while liste[index] != ",":
            if liste[index] != " " and liste[index] != "'":
                date.append(liste[index])
            index += 1

        index += 2

        while liste[index] != ",":
            if liste[index] != " " and liste[index] != "'":
                time_trans.append(liste[index])
            index += 1

        index += 2

        while liste[index] != ",":
            if liste[index] != " " and liste[index] != "'":
                name.append(liste[index])
            index += 1

        index += 2

        while liste[index] != ",":
            if liste[index] != " " and liste[index] != "'":
                category.append(liste[index])
            index += 1

        index += 2

        while liste[index] != ",":
            if liste[index] != " " and liste[index] != "'":
                account.append(liste[index])
            index += 1

        index += 2

        while liste[index] != "]":
            if liste[index] != " " and liste[index] != "'":
                id.append(liste[index])
            index += 1

        result.append("".join(amount))
        result.append("".join(date))
        result.append("".join(time_trans))
        result.append("".join(name))
        result.append("".join(category))
        result.append("".join(account))
        result.append("".join(id))
        return result


# init_example()
# t = TransactionListControl()
"""t.add_transaction(10, str(time.strftime('%d.%m.%y')), str(time.strftime('%H:%M:%S')), 'example', 'test1')
t.add_transaction(10, str(time.strftime('%d.%m.%y')), str(time.strftime('%H:%M:%S')), 'example1', 'test1')
t.add_transaction(10, str(time.strftime('%d.%m.%y')), str(time.strftime('%H:%M:%S')), 'example2', 'test1')
t.add_transaction(10, str(time.strftime('%d.%m.%y')), str(time.strftime('%H:%M:%S')), 'example3', 'test1')
t.add_transaction(-300, str(time.strftime('%d.%m.%y')), str(time.strftime('%H:%M:%S')), 'rent_jan', 'rent')
t.add_transaction(-200, str(time.strftime('%d.%m.%y')), str(time.strftime('%H:%M:%S')), 'car_jan', 'car')"""

# t.delete_transaction(1)
# t.delete_transaction(1)

"""print(t.return_all_needed(4, "car"))
print(t.total_sum())
print(t.transaction_list_work[-1][5] + " :id")
print(t.change_transaction(3, t.transaction_list_work[-2][5], "", "motor"))
t.save_listtransaction_file()"""
# print(t.transaction_list_work)
# print(len(t.transaction_list_work))
"""print("now")
for i in range(1000000):
    # print(i)
    # t.add_transaction(10, str(time.strftime('%d.%m.%y')), str(time.strftime('%H:%M:%S')), 'example1', 'test'+str(i))
    t.delete_transaction_by_index(-1)"""
# print(len(t.return_all_needed(2, '18:45:49')))
# t.save_listtransaction_to_file()
