def init_exemple():
    lc = open("usr_data/list_accounts.txt", "w")
    lc.writelines(str(["credit1", 1234, 150, 2]) + "\n")
    lc.writelines(str(["cash", 4564, 10.30, 1]) + "\n")
    lc.writelines(str(["debit1", 1232, 100.64, 3]) + "\n")
    lc.writelines(str(["home_savings", 7898, 10000, 4]) + "\n")


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

    def add_category(self, name, last_4_digits, amount, priority):
        """
        :param name: of the category
        :param last_4_digits: the last for digits of the acc, so you can see what acc it is, it's not necessary
        :param amount: what is the max to spend
        :param priority: will be needed when sorting for example in the AddTransactionScreen, to give the most
            used first
        """
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

    def find_prioraty(self, prio):
        """
        :param prio: the priority that is needed
        :return: gives the index from self.list_accounts back
        """
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
        for i in range(len(self.list_accounts) + 1):
            try:
                result.append(self.list_accounts[self.find_prioraty(i)])
            except:
                pass
        print(result)

    def change_account(self, name, index, new_info):
        """
        :param name: the (can also be the old) name by what we search the list_categories
        :param index: what field needs to be changing? 0:name; 1:spend_this_month; 2:max_per_month; 3: priority
        :param new_info: it's clear
        """
        self.find_account_by_name(name).change_category_self(index, new_info)

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
        :param liste: are the accounts item, that is a string in the .txt file so needs to be parsed
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
            result.append(float("".join(last_4_digits)))
        except:
            result.append("")
        try:
            result.append(float("".join(amount)))
        except:
            result.append(0)
        try:
            result.append((float("".join(priority))))
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


# init_exemple()
ac = AccountsControl()
# ac.add_category("debit2", "", "20.69", "")
# ac.delete_category(-1)
# print(ac.list_accounts[-1].name)
print(ac.find_account_by_name("cash"))
print(ac.list_accounts)
print(ac.list_accounts[ac.find_prioraty(1)])
ac.list_accounts_by_priority()
ac.change_account("cash", 2, 12.34)
ac.change_account("debit2", 3, 10)
ac.save_listaccounts_to_file()
