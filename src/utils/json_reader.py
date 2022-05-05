import json
import os

class JSONLoader:
    def __init__(self, file) -> None:
        #TODO: In terminal this will be a relative path, in IDE it will be an absolute path
        self.file = f"{os.getcwd()}/{file}"

    def read(self) -> dict:
        try:
            with open(self.file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            with open(self.file, 'x') as f:
                json.dump({}, f, indent=4)
            return {}

    def write(self, data: dict) -> None:
        try:
            with open(self.file, 'w') as f:
                json.dump(data, f, indent=4)
        except FileNotFoundError:
            with open(self.file, 'x') as f:
                json.dump(data, f, indent=4)