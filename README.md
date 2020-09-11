# yomiel

`yomiel` is the pretty printer for [jomiel] messages.

![Example (yomiel)](./docs/demo.svg)

## Features

- Support for authentication and encryption (CURVE and SSH)
- Support for different output formats (raw/json/yaml)
- Highly configurable

## Getting started

- `yomiel` requires [Python] 3.6+
- Make sure `jomiel` is running

To install `yomiel` from from [PyPI]:

```shell
pip install yomiel        # For the latest release
yomiel <uri ...>          # Inquiry meta data for the given URI
```

To run `yomiel` from the repository:

```shell
git clone https://github.com/guendto/jomiel-yomiel.git
cd jomiel-yomiel
pip install -e .
python yomiel <uri ...>   # Inquiry meta data for the specified URI
```

## HOWTO

### Authenticate and encrypt using CURVE (or SSH)

See (jomiel) [HOWTO].

## License

`yomiel` is licensed under the [Apache License version 2.0][aplv2].

## Acknowledgements

`yomiel` uses [pre-commit] and its many hooks to lint and format the
project files. See the .pre-commit-config.yaml file for details.

### Subprojects

`yomiel` has the following subtrees (see git-subtree):

- [src/yomiel/comm/](src/yomiel/comm/) of [jomiel-comm]
- [src/yomiel/kore/](src/yomiel/kore/) of [jomiel-kore]

[python]: https://www.python.org/about/gettingstarted/
[jomiel-comm]: https://github.com/guendto/jomiel-comm/
[jomiel-kore]: https://github.com/guendto/jomiel-kore/
[howto]: https://github.com/guendto/jomiel/#howto
[jomiel]: https://github.com/guendto/jomiel/
[aplv2]: https://www.tldrlegal.com/l/apache2
[pre-commit]: https://pre-commit.com/
[pypi]: https://pypi.org/
