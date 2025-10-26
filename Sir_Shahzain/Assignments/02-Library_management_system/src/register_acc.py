import json
from pathlib import Path

json_path = Path(__file__).parent.parent / "database" / "userInfo.json"

def reg_new_acc(name: str, password: str) -> None:
    """
This function registers new users by adding their credentials in root/database directory.

Args:
    name: str -> username of the user.
    password: str -> password of the user.

Return:
    None
""" 
    if json_path.exists():
        with open(json_path, "r", encoding="utf-8") as f:
            try:
                users = json.load(f)
            except json.JSONDecodeError:
                users = []
    else:
        users = []

    new_user = {
        "name": name,
        "password": password
    }

    for user in users:
        if user["name"] == name:
            user["password"] = password
            break
    else:
        users.append(new_user)

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4)

