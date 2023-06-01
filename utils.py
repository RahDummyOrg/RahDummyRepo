import json

def read_data(file_path: str):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return {k:v for k,v in data.items() if v is not None}
    except (FileNotFoundError, KeyError):
        print("Error: Please check your creds.json file")
        return {}
