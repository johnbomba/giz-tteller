from app import view   # imports from module folders are relative to the file being executed by python3 since main.py is at the top level, imports need to come from app. even for the files inside of app
from app import model


def run():
    model.load()    
    while True:
        user_account = login_menu()  # returns the logged in user or None for quit
        if user_account == None:  # login menu returns None if 'quit' is selected
            break
        else:
            main_menu(user_account)  # when the user exits the main menu they will go back to login

def login_menu():
    while True:
        view.print_login_menu()
        choice = view.login_prompt().strip()
        if choice not in ("1", "2", "3"):
            view.bad_login_input()
        elif choice == "3":
            view.goodbye()
            return None # return None for quit

        elif choice == "1":
            """ TODO: prompt for firstname, lastname, and pin, and confirm pin
            create the account and then tell the user what their new account number is """
            pass

        elif choice == "2":
            """ TODO: prompt functions to ask for account and PIN, use try, except
            to check for bad login """
            return model.login("012345", "1234")

def create_account():
    """ call this from the main login loop """
    pass

def login_attempt():
    """ call this from the main login loop """
    pass

def main_menu(user):
    while True:
        view.print_main_menu(user)
        choice = view.main_prompt()
        """ TODO: add bad input message """
        if choice == "4":
            user["balance"] += 1.0 # delete this, just demonstrating model.save()
            model.save(user)
            return
        """ TODO: implement the various options """
