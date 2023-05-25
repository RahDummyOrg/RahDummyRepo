import json

def read_data(file_path: str):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except (FileNotFoundError, KeyError):
        print("Error: Please check your creds.json file")
        return {}
