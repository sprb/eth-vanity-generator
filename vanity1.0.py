import csv
import dataclasses

import math
from eth_account import Account
import secrets

input = str(input('What are the vanity values? '))

print('''
Generating...
''')


def wallet_generation():
    infinite_num = 1
    for i in range(1000000000000):
        priv = secrets.token_hex(32)
        private_key = '0x' + priv
        acct = Account.from_key(private_key)
        wallet_address = acct.address
        varible = '0x' + input 
        if wallet_address[:len(varible)] == '0x' + input:
            #print(wallet_address)
            #print(private_key)
            data = [wallet_address, private_key]
            header = ['Address', 'Private Key']
            with open('vanity.csv', 'w', newline='') as vanity_csv:
                writer = csv.writer(vanity_csv)
                writer.writerow(header)
            with open('vanity.csv', 'a', newline='') as vanity_csv:
                writer = csv.writer(vanity_csv)
                writer.writerow(data)
            print('Vanity.csv is created! Make sure to copy PK and delete.')
            break
        else:
            print(infinite_num)
            infinite_num += 1
            continue
        
wallet_generation()