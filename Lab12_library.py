# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 01:33:00 2026

@author: Priyangan
"""

class BankSystem:
    def __init__(self, acc_id, balance, loan):
        self.__acc_id = acc_id
        self.__balance = balance
        self.__loan = loan
        
    def get_id(self):
        return self.__acc_id
    def get_balance(self):
        return self.__balance
    def get_loan(self):
        return self.__loan
    
    def deposit(self,amount):
        if amount >0 :
            self.__balance += amount
        else:
            print("Invalid Activity")
            
    def withdraw(self, amount):
        if amount>0 and self.__balance>=amount:
            self.__balance -= amount
        else:
            print("Invalid Activity")
            
    def take_loan(self, amount):
        if amount>0:
            self.__loan+=amount
            self.__balance+=amount
        else:
            print("Invalid Amount")
            
    def pay_loan(self,amount):
        if amount>0 and self.__loan>= amount and self.__balance>=amount:
            self.__loan-=amount
            self.__balance-=amount
        else:
            print("Invalid Amount")
    
    def transfer_amount(self,amount,acc):
        if amount>0 and self.__balance>=amount:
            self.__balance-=amount
            acc.deposit(amount)
        else:
            print("Invalid Activity")
        
            
            
            
         