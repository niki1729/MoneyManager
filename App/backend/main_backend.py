


class MainBackend:
    def __init__(self, transactions, categories, accounts):
        self.trans_list_controller = transactions
        self.categories_controller = categories
        self.accounts_controller = accounts

    def save_transaction(self, amount, date, time_trans, name, category, account):
        pass

