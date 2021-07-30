def init_exemple():
    lc = open("usr_data/list_categories.txt", "w")
    lc.writelines(str(["rent", 500, 1000, 3]) + "\n")
    lc.writelines(str(["clothing", 20.40, 50, 2]) + "\n")
    lc.writelines(str(["groceries", 50, 170, 1]) + "\n")
    lc.close()

class CategoriesControl:
    """
    Controls the Categories
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
        list_cat = open("usr_data/list_categories.txt", "a")
        list_cat.close()

        self.list_categories = []
        self.get_list_categ_from_txt()

    def get_list_categ_from_txt(self):
        """creates a list of Category Objects from the .txt file"""
        list_cat = open("usr_data/list_categories.txt", "r")
        for i in list_cat:
            intermediate = self.parser_string_to_category_item(i[:-1])
            self.list_categories.append(Category(intermediate[0], intermediate[1], intermediate[2], intermediate[3]))
        print(self.list_categories, "after parsing and creating objects")

    def add_category(self, name, spend_this_month, max_per_month, priority):
        """
        :param name: of the category
        :param spend_this_month: how much already spend
        :param max_per_month: what is the max to spend
        :param priority: will be needed when sorting for example in the AddTransactionScreen, to give the most
            used first
        """
        self.list_categories.append(Category(name, spend_this_month, max_per_month, priority))

    def delete_category(self, index):
        """
        :param index: deletes a transaction item by the index of the transaction_list_work NOT by the name
        """
        self.list_categories.pop(index)  # pop with index

    def save_listcategories_to_file(self):
        """
        Save the self.list_categories that we work with to the text file. We just completely overwrite the .txt file
        and if there (in the txt file) were more categories then we just overwrtie the last entires in the .txt file
        with empty strings ("")
        """
        len_txt_file = self.get_len_list_categories()
        len_transaction_list_work = len(self.list_categories)

        list_transaction = open("usr_data/list_categories.txt", "w")
        diff = len_transaction_list_work - len_txt_file
        print("diff" + str(diff))
        if diff <= 0:
            for i in self.list_categories:
                intermediate = [i.name, i.spend_this_month, i.max_per_month, i.priority]
                list_transaction.write(str(intermediate) + "\n")
        else:
            for i in self.list_categories:
                intermediate = [i.name, i.spend_this_month, i.max_per_month, i.priority]
                list_transaction.write(str(intermediate) + "\n")
            for i in range(diff):
                list_transaction.write("")
        list_transaction.close()

    def find_category_by_name(self, name):
        """
        :param name: the name you are searching after
        :return: the Account class
        """
        for i in range(len(self.list_categories)):
            if self.list_categories[i].name == name:
                return self.list_categories[i]

    def find_prioraty(self, prio):
        """
        :param prio: the priority that is needed
        :return: gives the index from self.list_categories back
        """
        for i in range(len(self.list_categories)):
            if float(self.list_categories[i].priority) == prio:
                return i
            else:
                pass

    def list_categories_by_priority(self):
        """
        :return: list of Category objects sorted by priority
        """
        result = []
        for i in range(len(self.list_categories) + 1):
            try:
                result.append(self.list_categories[self.find_prioraty(i)])
            except:
                pass
        print(result)

    def change_category(self, name, index, new_info):
        """
        :param name: the (can also be the old) name by what we search the list_categories
        :param index: what field needs to be changing? 0:name; 1:spend_this_month; 2:max_per_month; 3: priority
        :param new_info: it's clear
        """
        self.find_category_by_name(name).change_category_self(index, new_info)

    @staticmethod
    def get_len_list_categories():
        """
        :return: the length of the list_categories.txt
        """
        file = open("usr_data/list_categories.txt", "r")
        index = 0
        mot = "a"
        while mot != '':
            mot = file.readline()
            index = index + 1
        file.close()
        return int(index - 1)

    @staticmethod
    def parser_string_to_category_item(liste):
        """
        :param liste: are the categories item, that is a string in the .txt file so needs to be parsed
        :return: list with the category item not a string list
        """
        result = []
        index = 1  # we directly skipp [

        name = []
        spend_this_month = []
        max_per_month = []
        priority = []

        while liste[index] != ",":
            if liste[index] != " " and liste[index] != "'":
                name.append(liste[index])
            index += 1
        index += 2

        while liste[index] != ",":
            if liste[index] != " " and liste[index] != "'":
                spend_this_month.append(liste[index])
            index += 1
        index += 2

        while liste[index] != ",":
            if liste[index] != " " and liste[index] != "'":
                max_per_month.append(liste[index])
            index += 1
        index += 2

        while liste[index] != "]":
            if liste[index] != " " and liste[index] != "'":
                priority.append(liste[index])
            index += 1

        result.append("".join(name))
        result.append(float("".join(spend_this_month)))
        result.append(float("".join(max_per_month)))
        result.append((float("".join(priority))))

        return result


class Category:
    """
    Category Class with yet only few arguments but will probably will have a few functions later on
    """

    def __init__(self, name, spend_this_month, max_per_month, priority):
        self.name = name

        self.spend_this_month = spend_this_month
        self.max_per_month = max_per_month

        self.priority = priority

    def change_category_self(self, index, new_info):
        if index == 0:
            self.name = new_info
        if index == 1:
            self.spend_this_month = new_info
        if index == 2:
            self.max_per_month = new_info
        if index == 3:
            self.priority = new_info


# init_exemple()
cc = CategoriesControl()
# cc.add_category("dance", 15, 45, 4)
# print(cc.list_categories[3].name, "last")
# cc.get_len_list_categories()
# cc.delete_category(-1)
print(cc.list_categories)
cc.change_category("rent", 2, 2000)
cc.save_listcategories_to_file()
cc.list_categories_by_priority()
print(cc.find_category_by_name("dance"))
