import json
from pathlib import Path

def load_staff():
    json_path = Path(__file__).parent.parent / "database" / "staffInfo.json"
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)
    
def load_user():
    current_file = Path(__file__)
    json_path = current_file.parent.parent / "database" / "userInfo.json"
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)
    

def authentication(name: str, password: str, access_type: str) -> bool:

    if access_type not in ("user", "staff"):
        return False
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
    return False