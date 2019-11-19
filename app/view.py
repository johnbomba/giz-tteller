
def print_login_menu():
    print("""Welcome to Terminal Teller!:                                                       
                                                                                   
    1) create account                                                              
    2) log in                                                                      
    3) quit                                                                        
""")

def login_prompt():
    return input("Your choice:")

def bad_login_input():
    print("Input not recognized\n")

def goodbye():
    print("    Goodbye!\n")

def print_main_menu(user):
    print(f"""Hello, {user["first"]} {user["last"]} ({user["account_num"]})                                                    
                                                                                
    1 Check balance                                                       
    2 Withdraw funds                                                           
    3 Deposit funds                                                            
    4 Sign out
""")

def main_prompt():
    return input("Your choice:")