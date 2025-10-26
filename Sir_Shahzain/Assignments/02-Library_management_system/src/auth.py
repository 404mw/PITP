import json
from pathlib import Path

def load_staff():
    """
This function loads staff data from root/staffInfo.json

Args:
    None

Return:
    None    
"""
    json_path = Path(__file__).parent.parent / "database" / "staffInfo.json"
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)
    
def load_user():
    """
This function loads user data from root/userInfo.json

Args:
    None

Return:
    None
"""
    current_file = Path(__file__)
    json_path = current_file.parent.parent / "database" / "userInfo.json"
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)
    

def authentication(name: str, password: str, access_type: str = "user") -> bool | Exception:
    """
This function authenticates the user with their given username, password and access type.

Args:
    name: str -> username of the user
    passsword: str -> password of the user
    access_type: str (optional) -> "user" or "staff", defaults to "user"

Return:
    bool | Exception
"""

    if access_type not in ("user", "staff"):
        return ValueError(f"No role of {access_type} exists....")
    
    elif access_type == "staff":
        staff_info: list[dict] = list(load_staff())

        for info in staff_info:
            if (name == info["name"]) and (password == info["password"]):
                return True
            else:
                return False
    elif access_type == "user":
        user_info: list[dict] = list(load_user())
        for info in user_info:
            if (name == info["name"]) and (password == info["password"]):
                return True
            else:
                return False
    return Exception("Something went wrong....")