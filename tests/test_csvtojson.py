import csv
import json
import os
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from csvtojson import convert_csv_to_json

def test_csv_has_12_columns():
    with open('profiles1.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        assert len(header) == 12

def test_csv_has_900_plus_rows():
    with open('profiles1.csv', newline='', encoding='utf-8') as f:
        reader = list(csv.reader(f))
        assert len(reader) > 900  # includes header

def test_json_has_correct_structure():
    convert_csv_to_json()
    with open('docs/data.json', encoding='utf-8') as f:
        data = json.load(f)
        assert len(data) > 900
        assert isinstance(data[0], dict)
        assert len(data[0].keys()) == 12