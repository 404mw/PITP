from src.auth import authentication
from src.register_acc import reg_new_acc

print("===== Welcome to ABC Libarary =====\n")
print("Type 1 to access as a Staff Member")
print("Type 2 to access as a Customer")
user_input: str = input("Enter your choice here: ")

while not user_input.lower() == "q":
    
    # restart loop at invalid input 
    if user_input not in ("1", "2"):
        print("\nInvalid Choice")
        user_input: str = input("\nEnter your choice here: ")

    access: str = "staff" if user_input == "1" else "user"
    input_name: str = input("\nEnter your name: ")
    input_pass: str = input("Enter your password: ")
    if authentication(input_name, input_pass, access):
        print("\naccess granted")
    else:
        print("\naccess denied")
    
    if (access == "user"):
        print("We are glad to have you here: ")