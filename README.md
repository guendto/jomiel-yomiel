# yomiel

`yomiel` is the pretty printer for [jomiel] messages.

![Example (yomiel)](./docs/examples/yomiel-framed.svg)

## Table of Contents

<!-- vim-markdown-toc GFM -->

* [Features](#features)
* [Getting started](#getting-started)
* [HOWTO](#howto)
  * [Authenticate and encrypt using CURVE (or SSH)](#authenticate-and-encrypt-using-curve-or-ssh)
* [License](#license)
* [Acknowledgements](#acknowledgements)
  * [Subprojects](#subprojects)

<!-- vim-markdown-toc -->

## Features

* Support for authentication and encryption (CURVE and SSH)
* Support for different output formats (raw/json/yaml)
* Highly configurable

## Getting started

* `yomiel` requires [Python] 3.6+
* Make sure `jomiel` is running

To install `yomiel` from from [PyPI]:

```shell
pip install yomiel        # For the latest release
yomiel <uri ...>          # Inquiry meta data for the given URI
```

To run `yomiel` from the repository:

* Make sure you have installed protobuf compiler (debian:
  protobuf-compiler)

```shell
git clone https://github.com/guendto/jomiel-yomiel.git && cd jomiel-yomiel
pip install -r ./requirements.txt
python setup.py build_py  # Generate the protobuf message bindings
python yomiel <uri ...>   # Inquiry meta data for the specified URI
```

## HOWTO

### Authenticate and encrypt using CURVE (or SSH)

See (jomiel) [HOWTO].

## License

`yomiel` is licensed under the [Apache License version 2.0][APLv2].

## Acknowledgements

* Linted by [flake8], [yamllint] and [markdownlint]
* Formatted by [black]

### Subprojects

`yomiel` subtrees (includes) the following subprojects:

* [jomiel-proto] (yomiel/comm/proto)
* [jomiel-comm]  (yomiel/comm)
* [jomiel-kore]  (yomiel/kore)

[markdownlint]: https://github.com/markdownlint/markdownlint
[jomiel-proto]: https://github.com/guendto/jomiel-proto/
[Python]: https://www.python.org/about/gettingstarted/
[jomiel-comm]: https://github.com/guendto/jomiel-comm/
[jomiel-kore]: https://github.com/guendto/jomiel-kore/
[HOWTO]: https://github.com/guendto/jomiel/#howto
[yamllint]: https://pypi.org/project/yamllint/
[jomiel]: https://github.com/guendto/jomiel/
[APLv2]: https://www.tldrlegal.com/l/apache2
[flake8]: https://pypi.org/project/flake8/
[black]: https://pypi.org/project/black/
[PyPI]: https://pypi.org/
