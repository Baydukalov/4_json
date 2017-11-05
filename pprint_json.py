import json
import sys


def load_data(filepath):
    with open(filepath, 'r') as json_file:
        return json.load(json_file)


def pretty_print_json(json_file):
    return json.dumps(json_file, indent=4, ensure_ascii=False, sort_keys=True)


if __name__ == '__main__':
    full_path = sys.argv[1]
    print(pretty_print_json(load_data(full_path)))
