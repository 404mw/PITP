from src.auth import authentication
from src.register_acc import reg_new_acc
from src.classes.library import Library

print("===== Welcome to ABC Libarary =====\n1. Login\n2. Register\n3. Exit\n")
user_input: str = input("Enter your choice here: ")

session: dict = {
    "has_started": False,
    "access": None
}

while not user_input.lower() == "3":
    # restart loop on invalid input
    if user_input not in ("1", "2"):
        print("\nInvalid Option")
        user_input: str = input("\nEnter your choice here: ")
    
    # Initializing the library instance 
    library: Library = Library()

    # Login Block
    if user_input == "1":

        input_name: str = input("\nEnter your name: ")
        input_pass: str = input("Enter your password: ")
        input_access: str = input("\nSelect Your Access Type:\n1. User\n2. Staff")
        if input_access not in ("1", "2"):
            print("\nInvalid Option")
            input_access: str = input("Select Your Access Type:\n1. User\n2. Staff")

        access: str = "staff" if user_input == "2" else "user"

        # Authenticating with the provided info
        if authentication(input_name, input_pass, access):
            print("\nAccess Granted")
        else:
            print("\nInvalid credentials, access denied")

        # User level Block
        if access == "user":
            print("\n1. View available books\n2. Rent a book\n3. Return a book\n4. Logout")


     
    # 

    # 
    # input_name: str = input("\nEnter your name: ")
    # input_pass: str = input("Enter your password: ")
    # 
    
    # if (access == "user"):
    #     print("We are glad to have you here: ")