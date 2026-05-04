# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 01:33:28 2026

@author: Priyangan
"""
from Lab12_library import BankSystem

acc1=BankSystem(401, 500, 0)
acc2=BankSystem(402, 500, 0)
acc_details=[acc1, acc2]

for acc in acc_details:
    acc.deposit(100)
    
for acc in acc_details:
    acc.withdraw(50)
    
for acc in acc_details:
    acc.take_loan(200)
        
for acc in acc_details:
    print(acc.get_id(), acc.get_balance(), acc.get_loan())
        
for acc in acc_details:
    acc.pay_loan(100)
    
acc1.transfer_amount(150, acc2)

for acc in acc_details:
    print(acc.get_id(), acc.get_balance(),acc.get_loan())
    