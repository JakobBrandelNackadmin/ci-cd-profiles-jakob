import csv
import json

def convert_csv_to_json(csv_file='profiles1.csv', json_file='docs/data.json'):
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(rows, f, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    convert_csv_to_json()