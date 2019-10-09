# yomiel

`yomiel` is the pretty printer for [jomiel][1] messages.

![Example (yomiel)](./docs/examples/yomiel-framed.svg)

## Features

- Support for authentication and encryption (CURVE and SSH)
- Support for different output formats (raw/json/yaml)
- Highly configurable

## Getting started

- **`yomiel` requires [Python 3.5+][22]**
- **Make sure `jomiel` is running**

To install `yomiel` from from [PyPI][24]:

```shell
pip install yomiel        # For the latest release
yomiel <uri ...>          # Inquiry meta data for the given URI
```

To run `yomiel` from the repository:

- Make sure you have installed protobuf compiler first (debian:
  protobuf-compiler)

```shell
git clone https://github.com/guendto/jomiel-yomiel.git && cd jomiel-yomiel
pip install -r ./requirements.txt
python setup.py build_py  # Generate the protobuf message bindings
python yomiel <uri ...>   # Inquiry meta data for the specified URI
```

## License

`yomiel` is licensed under the [Apache License version 2.0][23] (APLv2).

## HOWTO

### Authentication and encryption using CURVE / SSH

See the [HOWTO][10] section of [jomiel][1] for the instructions.

## Development notes

### Subprojects

`yomiel` includes (as `git-subtree`) the following subprojects within
the subdirectories:

- [jomiel-proto.git][3] (yomiel/comm/proto)
- [jomiel-comm.git][2]  (yomiel/comm)
- [jomiel-kore.git][4]  (yomiel/kore)

### Acknowledgements

- Linted by [pylint][25], [flake8][26] and [yamllint][27]
- Formatted by [yapf][28]

[1]: https://github.com/guendto/jomiel/
[2]: https://github.com/guendto/jomiel-comm/
[3]: https://github.com/guendto/jomiel-proto/
[4]: https://github.com/guendto/jomiel-kore/
[10]: https://github.com/guendto/jomiel/#howto
[22]: https://www.python.org/about/gettingstarted/
[23]: https://tldrlegal.com/license/apache-license-2.0-(apache-2.0)
[24]: https://pypi.org/
[25]: https://pypi.org/project/pylint/
[26]: https://pypi.org/project/flake8/
[27]: https://pypi.org/project/yamllint/
[28]: https://pypi.org/project/yapf/
