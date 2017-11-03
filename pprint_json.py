import json


def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)

def pretty_print_json(data):
    print(json.dumps(data, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    filepath = input(':   ')
    pretty_print_json(load_data(filepath))