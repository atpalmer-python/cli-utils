# dataformat-cli

## Usage

```
Usage: dataformat [OPTIONS]

Options:
  -i, --in [json|prettyjson|yaml|toml]
                                  Format of data written to STDOUT
  -o, --out [json|prettyjson|yaml|toml]
                                  Format of data read from STDIN
  --help                          Show this message and exit.

```

## Usage Samples

Convert JSON to YAML: 
```
$ dataformat -o yaml < mydata.json > mydata.yaml
```

Convert YAML to TOML:
```
$ dataformat -i yaml -o toml < mydata.yaml > mydata.toml
```

Pipe from JSON web APIs:
```
$ curl -s httpbin.org/get | dataformat -o yaml
args: {}
headers: {Accept: '*/*', Host: httpbin.org, User-Agent: curl/7.58.0}
origin: 127.0.0.1
url: https://httpbin.org/get
```
