import yaml


def dump(data, f):
    return yaml.dump(data, f)


def load(f):
    return yaml.safe_load(f)
