import os
import json


def load_recommendation(option):
    DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'recommendations')
    file_path = os.path.join(DATA_DIR, f"{option}.json")
    
    if not os.path.exists(file_path):
        return None

    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)