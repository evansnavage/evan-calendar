import os
import json
from datetime import datetime

JSON_DIR = './json/'

def read_json(file_name):
    file_path = os.path.join(JSON_DIR, file_name)
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r') as file:
        return json.load(file)

def read_all():
    array = []
    for file_name in os.listdir(JSON_DIR):
        if file_name.endswith(".json"):
            file_path = os.path.join(JSON_DIR, file_name)
            with open(file_path, 'r') as file:
                array.append(json.load(file))
    return array

def write_json(file_name, data):
    file_path = os.path.join(JSON_DIR, file_name)
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def update_json(file_name, data):
    file_path = os.path.join(JSON_DIR, file_name)
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r+') as file:
        file_data = json.load(file)
        file_data.update(data)
        file.seek(0)
        json.dump(file_data, file, indent=4)

def delete_json(file_name):
    file_path = os.path.join(JSON_DIR, file_name)
    if os.path.exists(file_path):
        os.remove(file_path)
        return True
    return False


def filter_date_range(start_date: str, end_date: str):
    """Takes in two date strings in the format 'YYYY-MM-DD'
    Returns all events in that date range, expensive in JSON."""
    all_events = read_all()
    filtered_events = []
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')

    if (end < start):
        return None
    for event in all_events:
        event_date = datetime.strptime(event['date'], '%Y-%m-%d')
        if start <= event_date <= end:
            filtered_events.append(event)

    return filtered_events