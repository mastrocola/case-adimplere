import json
import os


def get_mocks(folder):
    output = []

    for file_name in [file for file in os.listdir(folder) if file.endswith('.json')]:
        with open(f'{folder}/{file_name}', encoding='utf-8') as file:
            file_json = json.load(file)

            output.extend({**obj} for obj in file_json)

    return output
