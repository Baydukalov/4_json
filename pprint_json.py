import json


def load_data(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

def pretty_print_json(data):
    return json.dumps(data, indent=4, ensure_ascii=False, sort_keys=True)


if __name__ == '__main__':
    filepath = input('enter the path to the file:   ')
    pretty_print_json(load_data(filepath))