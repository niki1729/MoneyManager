def init_example():
    lc = open("usr_data/list_accounts.txt", "w")
    lc.writelines(str(["cash", 4564, 10.30, 1]) + "\n")
    lc.writelines(str(["credit1", 1234, 150, 2]) + "\n")
    lc.writelines(str(["debit1", 1232, 100.64, 3]) + "\n")
    lc.writelines(str(["home_savings", 7898, 100.01, 4]) + "\n")


class AccountsControl:
    """
    Controls the Accounts

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
        list_acc = open("usr_data/list_accounts.txt", "a")
        list_acc.close()

        self.list_accounts = []
        self.get_list_acc_from_txt()

    def get_list_acc_from_txt(self):
        """creates a list of Accounts Objects from the .txt file"""
        list_acc = open("usr_data/list_accounts.txt", "r")
        for i in list_acc:
            intermediate = self.parser_string_to_account_item(i[:-1])
            self.list_accounts.append(Account(intermediate[0], intermediate[1], intermediate[2], intermediate[3]))
        print(self.list_accounts, "after parsing and creating objects")
        for i in range(len(self.list_accounts)):
            print(self.list_accounts[i].name, end="     ")
        print("names first")

    def add_category(self, name, last_4_digits, amount, priority):
        """
        :param name: of the category
        :param last_4_digits: the last for digits of the acc, so you can see what acc it is, it's not necessary
        :param amount: how much is there
        :param priority: will be needed when sorting for example in the AddTransactionScreen, to give the most
            used first
        """
        # TODO: need one function that will control if the data in the input is correct
        self.list_accounts.append(Account(name, last_4_digits, amount, priority))

    def delete_category(self, index):
        """
        :param index: deletes a account by the index of the transaction_list_work NOT by the name
        """
        self.list_accounts.pop(index)  # pop with index

    def save_listaccounts_to_file(self):
        """
        Save the self.list_accounts that we work with to the text file. We just completely overwrite the .txt file
        and if there (in the txt file) were more categories then we just overwrtie the last entires in the .txt file
        with empty strings ("")
        """
        self.list_accounts = self.list_accounts_by_priority()
        print(self.list_accounts, "save_listaccouns_to file")

        len_txt_file = self.get_len_list_accounts()
        len_accounts_list_work = len(self.list_accounts)

        list_accs = open("usr_data/list_accounts.txt", "w")
        diff = len_accounts_list_work - len_txt_file
        print("diff" + str(diff))
        if diff <= 0:
            for i in self.list_accounts:
                intermediate = [i.name, i.last_4_digits, i.amount, i.priority]
                list_accs.write(str(intermediate) + "\n")
        else:
            for i in self.list_accounts:
                intermediate = [i.name, i.last_4_digits, i.amount, i.priority]
                list_accs.write(str(intermediate) + "\n")
            for i in range(diff):
                list_accs.write("")
        list_accs.close()

    def find_account_by_name(self, name):
        """
        :param name: the name you are searching after
        :return: the Category class
        """
        for i in range(len(self.list_accounts)):
            if self.list_accounts[i].name == name:
                return self.list_accounts[i]

    def find_priority(self, prio):
        """
        :param prio: the priority that is needed
        :return: gives the index from self.list_accounts back
        """
        # TODO: need on function that can tell the highest/lowest priority and rearrange priorities

        for i in range(len(self.list_accounts)):
            if float(self.list_accounts[i].priority) == prio:
                return i
            else:
                pass

    def list_accounts_by_priority(self):
        """
        :return: list of Account objects sorted by priority
        """
        result = []
        for i in range(self.list_accounts[self.lowest_priority()].priority + 1):
            try:
                result.append(self.list_accounts[self.find_priority(i)])
            except:
                pass
        return result

    def highest_priority(self):
        """
        index must be set to 0 because if the first one has the highest priority, then if index is set to None, the
        return is None, and we don't want it
        :return gives the index from self.list_accounts back of the highest priority account
        """

        high_prio = self.list_accounts[0].priority
        index = 0
        for i in range(len(self.list_accounts)):
            if self.list_accounts[i].priority < high_prio:
                index = i
                high_prio = self.list_accounts[i].priority
        return index

    def lowest_priority(self):
        """
        :return gives the index from self.list_accounts back of the lowest priority account
        """
        lowest_prio = self.list_accounts[0].priority
        index = 0
        for i in range(len(self.list_accounts)):
            if self.list_accounts[i].priority > lowest_prio:
                index = i
                lowest_prio = self.list_accounts[i].priority
        return index

    def change_account(self, name, index, new_info):
        """
        :param name: the (can also be the old) name by what we search the list_categories
        :param index: what field needs to be changing? 0:name; 1:spend_this_month; 2:max_per_month; 3: priority
        :param new_info: it's clear
        """
        self.find_account_by_name(name).change_category_self(index, new_info)

    def change_two_accounts_by_prio(self, ind1, ind2):
        """
        :param ind1:
        :param ind2:
        :return: nothing, the list now has different sorting
        """

        print(self.list_accounts, "in change two acc_by_prio")
        interm = self.list_accounts[ind1].priority
        self.list_accounts[ind1].priority = self.list_accounts[ind2].priority
        self.list_accounts[ind2].priority = interm

        self.list_accounts_by_priority()

    def enter_after_prio(self, index, prio):
        """
        :param index: of the element that is already in the list but needs to change priority drastically
        :param prio: the new prio
        :return:
        """
        element = self.list_accounts[index]
        print(self.list_accounts[index], "printed what need to be element")
        print(element.name, "element, why without name")
        print(self.list_accounts[self.highest_priority()].priority, "enter_after_prio")
        self.list_accounts.pop(index)  # pop with index
        print(self.list_accounts, "after pop")
        if prio > self.list_accounts[self.lowest_priority()].priority:
            element.priority = self.lowest_priority() - 1
            print(element.priority, "element prio")
            self.list_accounts.append(element)
            self.change_priority_after_index(index)
            print("prio>lowest")
            return
        if prio < self.list_accounts[self.highest_priority()].priority:
            print("prio<highest prio")
            result = [element]
            for i in self.list_accounts:
                result.append(i)

            self.list_accounts = result
            print(result)
            return
        else:
            print("mid")
            ind = 0
            result = []
            while self.list_accounts[ind].priority <= prio:
                result.append(self.list_accounts[ind])
                ind += 1
            result.append(element)

            for i in range(len(self.list_accounts) - ind):
                result.append(self.list_accounts[i + ind])

    def change_priority_after_index(self, ind):
        """
        this function will add to all self.list_accounts elements after the index +1 to priorities
        :param ind: after what index from self.list_accounts the priority needs to change
        :return: nothing, self.list_accounts has now new priorities
        """
        ind+=1
        # TODO see better with +1 or -1 here
        for i in range(len(self.list_accounts) - ind):
            self.list_accounts[i + ind].priority += 1

    @staticmethod
    def get_len_list_accounts():
        """
        :return: the length of the list_accounts.txt
        """
        file = open("usr_data/list_accounts.txt", "r")
        index = 0
        mot = "a"
        while mot != '':
            mot = file.readline()
            index = index + 1
        file.close()
        return int(index - 1)

    @staticmethod
    def parser_string_to_account_item(liste):
        """
        :param liste: are the account item, that is a string in the .txt file so needs to be parsed
        :return: list with the account item not a string list
        """
        result = []
        index = 1  # we directly skipp [

        name = []
        last_4_digits = []
        amount = []
        priority = []

        while liste[index] != ",":
            if liste[index] != " " and liste[index] != "'":
                name.append(liste[index])
            index += 1
        index += 2

        while liste[index] != ",":
            if liste[index] != " " and liste[index] != "'":
                last_4_digits.append(liste[index])
            index += 1
        index += 2

        while liste[index] != ",":
            if liste[index] != " " and liste[index] != "'":
                amount.append(liste[index])
            index += 1
        index += 2

        while liste[index] != "]":
            if liste[index] != " " and liste[index] != "'":
                priority.append(liste[index])
            index += 1
        try:
            result.append("".join(name))
        except:
            pass
        try:
            result.append(int("".join(last_4_digits)))
        except:
            result.append("")
        try:
            result.append(float("".join(amount)))
        except:
            result.append(0)
        try:
            result.append((int("".join(priority))))
        except:
            result.append(100)

        return result


class Account:
    def __init__(self, name, l_4_digits, amount, priority):
        self.name = name
        self.last_4_digits = l_4_digits
        self.amount = amount
        self.priority = priority

    def change_category_self(self, index, new_info):
        if index == 0:
            self.name = new_info
        if index == 1:
            self.last_4_digits = new_info
        if index == 2:
            self.amount = new_info
        if index == 3:
            self.priority = new_info


init_example()
ac = AccountsControl()
# ac.add_category("home saving", 7898, 1234.56, 10)
# ac.save_listaccounts_to_file()
# ac.delete_category(-1)
# print(ac.list_accounts[-1].name)
# print(ac.find_account_by_name("cash"))
# print(ac.list_accounts)
# print(ac.list_accounts[ac.find_prioraty(1)])
# ac.list_accounts_by_priority()
# ac.change_account("cash", 2, 12.34)
# ac.change_account("debit2", 3, 10)
# print(ac.list_accounts[ac.highest_priority()].name, "highest prio")
# print(ac.list_accounts[ac.find_priority(3)].name, "find prio")
# print(ac.list_accounts[ac.lowest_priority()].name, "lowest prio")
# print(ac.list_accounts_by_priority())
"""for i in ac.list_accounts:
    print(i.priority)"""
# print(ac.highest_priority())
# ac.change_two_accounts_by_prio(1, 4)
# ac.change_two_accounts_by_prio(2, 5)
ac.enter_after_prio(2, 1)
# ac.change_priority_after_index(0)
print(ac.list_accounts, "after enter_prio")
ac.save_listaccounts_to_file()
