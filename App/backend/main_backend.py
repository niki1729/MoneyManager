from categories_control import CategoriesControl, Category
from transaction_list_control import TransactionListControl


class MainBackend:
    def __init__(self):
        self.trans_list_contr = TransactionListControl()
        self.categories_contr = CategoriesControl()

        print(self.trans_list_contr.total_sum())
        self.trans_list_contr.change_transaction(4, self.trans_list_contr.transaction_list_work[-1][5], "", "clothes")
        self.trans_list_contr.change_transaction(0, self.trans_list_contr.transaction_list_work[-3][5], "", -123)
        print(self.trans_list_contr.find_after_ind_and_criteria(4, "car"))
        self.trans_list_contr.save_listtransaction_to_file()


MainBackend()
