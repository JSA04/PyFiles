import store
from typing import List


class Account:
    def __init__(self, number: int, holder: str, balance: float, limit: int):
        self.__number: int = number
        self.__holder: str = holder
        self.__balance: float = balance
        self.__limit: int = limit
        self.__propertys: List[str] = []

    def extract(self):
        print(f"Balance of U${self.__balance} of holder {self.__holder}")

    def deposit(self, value):
        self.__balance += value

    def can_withdraw(self, value_to_withdraw):
        return value_to_withdraw <= (self.limit + self.__balance)

    def withdraw(self, value):
        if self.can_withdraw(value):
            self.__balance -= value
            return True
        else:
            print(F'The Value {value} exceeded your limit, which is '
                  F'{self.__limit}')
            return False

    def transfer(self, beneficiary, value):
        self.__balance -= value
        beneficiary.__balance += value

    @property
    def balance(self):
        return self.__balance

    @property
    def holder(self):
        return self.__holder

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, new_limit):
        self.__limit = new_limit

    def _buy(self):
        store.buy(self)

    @staticmethod
    def print_items(categoria="NONE"):
        store.print_items(categoria)

    @property
    def propertys(self):
        return self.__propertys

    def __str__(self):
        return f"The holder {self.holder} has U${self.balance} of " \
               f"Balance and U${self.limit} of Limit."
