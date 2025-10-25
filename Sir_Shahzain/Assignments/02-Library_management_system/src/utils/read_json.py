import json
from pathlib import Path

def read_json(target_file_name: str):
    json_path = Path(__file__).parent.parent / "database" / target_file_name
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)