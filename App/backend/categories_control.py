def init_exemple():
    lc = open("usr_data/list_categories.txt", "w")
    lc.writelines(str(["groceries", 50, 170, 1]) + "\n")
    lc.writelines(str(["clothing", 20.40, 50, 2]) + "\n")
    lc.writelines(str(["rent", 500, 1000, 3]) + "\n")
    lc.writelines(str(["dance", 30, 70, 4]) + "\n")
    lc.writelines(str(["sport", 15, 45, 30]) + "\n")
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
        list_cat = open("backend/usr_data/list_categories.txt", "a")
        list_cat.close()

        self.list_categories = []
        self.get_list_categ_from_txt()

    def get_list_categ_from_txt(self):
        """creates a list of Category Objects from the .txt file"""
        list_cat = open("backend/usr_data/list_categories.txt", "r")

        for i in list_cat:
            intermediate = self.parser_string_to_category_item(i[:-1])
            self.list_categories.append(Category(intermediate[0], intermediate[1], intermediate[2], intermediate[3]))
        print(self.list_categories, "after parsing and creating objects")
        for i in range(len(self.list_categories)):
            print(self.list_categories[i].name, end="     ")
        print("names first")

    def add_category(self, name, spend_this_month, max_per_month, priority):
        """
        :param name: of the category
        :param spend_this_month: how much already spend
        :param max_per_month: what is the max to spend
        :param priority: will be needed when sorting for example in the AddTransactionScreen, to give the most
            used first
        """
        # TODO: need one function that will control if the data in the input is correct
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
        self.list_categories = self.list_categories_by_priority()
        print(self.list_categories, "save_listaccouns_to file")

        len_txt_file = self.get_len_list_categories()
        len_transaction_list_work = len(self.list_categories)

        list_transaction = open("backend/usr_data/list_categories.txt", "w")
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
        # TODO: need on function that can tell the highest/lowest priority and rearrange priorities
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
        for i in range(self.list_categories[self.lowest_priority()].priority + 1):
            # TODO: see what is wrong here and why +2 and not +1
            try:
                result.append(self.list_categories[self.find_prioraty(i)])
            except:
                pass
        return result

    def highest_priority(self):
        """
        :return gives the index from self.list_categories back of the highest priority account
        """
        high_prio = self.list_categories[0].priority
        index = 0
        for i in range(len(self.list_categories)):
            if self.list_categories[i].priority < high_prio:
                index = i
                high_prio = self.list_categories[i].priority
        return index

    def lowest_priority(self):
        """
        :return gives the index from self.list_categories back of the lowest priority account
        """
        lowest_prio = self.list_categories[0].priority
        index = 0
        for i in range(len(self.list_categories)):

            if self.list_categories[i].priority > lowest_prio:
                lowest_prio = self.list_categories[i].priority
                index = i
        return index

    def change_category(self, name, index, new_info):
        """
        :param name: the (can also be the old) name by what we search the list_categories
        :param index: what field needs to be changing? 0:name; 1:spend_this_month; 2:max_per_month; 3: priority
        :param new_info: it's clear
        """
        self.find_category_by_name(name).change_account_self(index, new_info)

    def change_two_categories_by_prio(self, ind1, ind2):
        """
        :param ind1:
        :param ind2:
        :return: nothing, the list now has different sorting
        """

        print(self.list_categories, "in change two cat_by_prio")
        interm = self.list_categories[ind1].priority
        print(interm, self.list_categories[ind1].name, self.list_categories[ind2].name)
        self.list_categories[ind1].priority = self.list_categories[ind2].priority
        self.list_categories[ind2].priority = interm

        self.list_categories_by_priority()

    def enter_after_prio(self, index, prio):
        """
        :param index: of the element that is already in the list but needs to change priority drastically
        :param prio: the new prio, will be +1. more precis, its the prio of the one item after what the new item is
            placed
        :return:
        """
        element = self.list_categories[index]
        print(self.list_categories[index], "printed what need to be element")
        print(element.name, "element, why without name")
        print(self.list_categories[self.lowest_priority()].priority, "enter_after_prio")
        self.list_categories.pop(index)  # pop with index
        print(self.list_categories, "after pop")
        if prio > self.list_categories[self.lowest_priority()].priority:
            element.priority = self.list_categories[self.lowest_priority()].priority + 1
            print(element.priority, "element prio")
            self.list_categories.append(element)
            # self.change_priority_after_index(index)
            print("prio>lowest")
            return
        print(self.highest_priority(), "hi prio")
        if prio < self.list_categories[self.highest_priority()].priority:
            print("prio<highest prio")
            element.priority = self.list_categories[self.highest_priority()].priority - 1
            result = [element]
            for i in self.list_categories:
                result.append(i)

            self.list_categories = result
            print(result)
            return
        else:
            element.priority = prio
            print("mid")
            ind = 0
            result = []
            element.priority = prio + 1
            print(self.list_categories, "after_else")

            while self.list_categories[ind].priority <= prio:
                print(self.list_categories[ind].name)
                result.append(self.list_categories[ind])
                ind += 1
            print(element.name, element.priority)
            print(element, "element")
            result.append(element)
            print(result, "result before finish")
            for i in range(len(self.list_categories) - ind):
                self.list_categories[i + ind].priority += 1
                print(self.list_categories[i + ind].name, self.list_categories[i + ind].priority)

                result.append(self.list_categories[i + ind])

            self.list_categories = result

    def change_priority_after_index(self, ind):
        """
        this function will add to all self.list_categories elements after the index +1 to priorities
        :param ind: after what index from self.list_categories the priority needs to change
        :return: nothing, self.list_categories has now new priorities
        """
        ind += 1
        # TODO see better with +1 or -1 here
        for i in range(len(self.list_categories) - ind):
            self.list_categories[i + ind].priority += 1

    def rearrange_priorities(self):
        """
        :return: the self.list_accounts with priorities starting from 1 till len(self.list_accounts
        """
        result = []
        prio = 1
        for i in self.list_categories:
            i.priority = prio
            print(i.priority)
            prio += 1
            result.append(i)

        self.list_categories = result

    @staticmethod
    def get_len_list_categories():
        """
        :return: the length of the list_categories.txt
        """
        file = open("backend/usr_data/list_categories.txt", "r")
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
        result.append(int("".join(priority)))

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
# cc = CategoriesControl()
# cc.add_category("sport", 15, 45, 30)
# print(cc.list_categories[cc.lowest_priority()].name)
# print(cc.list_categories[3].name, "last")
# cc.get_len_list_categories()
# cc.delete_category(-1)
# print(cc.list_categories, "printcc-list categories")
# cc.change_category("rent", 2, 2000)
# cc.list_categories_by_priority()
# print(cc.find_category_by_name("dance"))
# cc.change_two_categories_by_prio(1, 4)
# cc.change_two_categories_by_prio(3, 2)
# cc.change_priority_after_index()
# cc.enter_after_prio(1, 3)
# cc.rearrange_priorities()
# cc.save_listcategories_to_file()

"""
['groceries', 50.0, 170.0, 1]
['clothing', 20.4, 50.0, 2]
['rent', 500.0, 1000.0, 3]
['dance', 30.0, 70.0, 4]
['sport', 15.0, 45.0, 30]
"""
