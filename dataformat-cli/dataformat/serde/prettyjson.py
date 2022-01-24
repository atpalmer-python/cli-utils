import json


def dump(data, f):
    return json.dump(data, f, indent=2)


def load(f):
    return json.load(f)
