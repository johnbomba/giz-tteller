import json
import os

BASEDIR = os.path.dirname(__file__)
DBFILENAME = "accounts.json"
DBPATH = os.path.join(BASEDIR, DBFILENAME)

class Account:

    def __init__(self, **kwargs):
        self.account_number = kwargs.get("account_number") # if "account_number" is in kwargs, set self.account_number to that, otherwise set self.account_number to None
        self.first_name = kwargs.get("first_name")
        self.last_name = kwargs.get("last_name")
        self.pin = kwargs.get("pin")
        self.balance = kwargs.get("balance", 0.0) # if you need a default value that is a mutable structure like a list or dict, you need to use a defaultdict from the collections module

        #print(kwargs)
    
    def save(self):
        try:
            with open(DBPATH, "r") as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            data = {}
        
        account_data = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "pin": self.pin,
            "balance": self.balance,
            "account_number": self.account_number
        }

        data[self.account_number] = account_data

        with open(DBPATH, "w") as json_file:
            json.dump(data, json_file, indent=2)