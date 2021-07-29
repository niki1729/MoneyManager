import time
from random import randint

list_transaction = open("usr_data/list_transactions.txt", "a")
list_transaction.close()


def init_example():
    list_transaction = open("usr_data/list_transactions.txt", "w")
    n = ['rent', 'insurance', 'car', 'eat', 'clothes']
    for i in range(5):
        list_transaction.write(
            str([i * 100, str(time.strftime('%d.%m.%y')), str(time.strftime("%H:%M:%S")), 'name' + str(i), n[i],
                 '{0}{1}{2}'.format(str(time.strftime('%d%m%y')),
                                    str(time.strftime('%H%M%S')), str(randint(1000000, 9999999)))]) + "\n")
    list_transaction.close()


class TransactionListControl:
    def __init__(self):
        self.transaction_list_work = []
        list_transaction = open("usr_data/list_transactions.txt", "r")
        for i in list_transaction:
            self.transaction_list_work.append(self.parser_string_to_transaction_item1(i[:-1]))
        list_transaction.close()
        # print(self.get_len_list_transaction())    works
        # print(self.transaction_list_work[5][2])

    def add_transaction(self, amount, date, time_trans, name, category):
        self.transaction_list_work.append([amount, date, time_trans, name, category,
                                           "{0}{1}{2}".format(str(time.strftime("%d%m%y")),
                                                              str(time.strftime("%H%M%S")),
                                                              str(randint(1000000000, 9999999999)))])
        # the last one is the id, created with date and time when created and random number (nearly perfect)
        print(self.transaction_list_work)

    def delete_transaction(self, index):
        self.transaction_list_work.pop(index)  # pop with index

        # self.transaction_list_work.remove(index) # remove the first occurrence

        print(self.transaction_list_work)

    def save_listtransaction_file(self):
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

    def return_all_needed(self, index, criteria):
        """

        :param index: is the index from the list (so 0 for costs till 5 id)
        :param criteria: what is asked more precisely
        :return:
        """
        result = []
        for i in self.transaction_list_work:
            print(i)
            if i[index] == criteria:
                result.append(i)
        return result

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

    def get_len_list_transaction(self):
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

    def parser_string_to_transaction_item1(self, liste):
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

        while liste[index] != "]":
            if liste[index] != " " and liste[index] != "'":
                id.append(liste[index])
            index += 1

        result.append("".join(amount))
        result.append("".join(date))
        result.append("".join(time_trans))
        result.append("".join(name))
        result.append("".join(category))
        result.append("".join(id))
        return result


init_example()
t = TransactionListControl()
t.add_transaction(10, str(time.strftime('%d.%m.%y')), str(time.strftime('%H:%M:%S')), 'example', 'test1')
t.add_transaction(10, str(time.strftime('%d.%m.%y')), str(time.strftime('%H:%M:%S')), 'example1', 'test1')
t.add_transaction(10, str(time.strftime('%d.%m.%y')), str(time.strftime('%H:%M:%S')), 'example2', 'test1')
t.add_transaction(10, str(time.strftime('%d.%m.%y')), str(time.strftime('%H:%M:%S')), 'example3', 'test1')
t.add_transaction(-300, str(time.strftime('%d.%m.%y')), str(time.strftime('%H:%M:%S')), 'rent_jan', 'rent')
t.add_transaction(-200, str(time.strftime('%d.%m.%y')), str(time.strftime('%H:%M:%S')), 'car_jan', 'car')

# t.delete_transaction(1)
t.delete_transaction(1)
t.save_listtransaction_file()
print(t.return_all_needed(4, "test1"))
print(t.total_sum())
