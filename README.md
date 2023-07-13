[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: LGPL v3](https://img.shields.io/badge/License-LGPL_v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)

**This repo is under development which is not complete yet.**

# Dri

Dri is a wrapper for the DaVinci Resolve Scripting API that provides auto-completion,
static type checking, and improved documentation. It packages all the APIs based on the
latest [README](READMEs), enhances them with well-formatted
docstrings (in NumPy style), and adds detailed type hints. This allows developers to
easily view parameter types and return value types for each API, while also enabling
static type checking tools like [mypy](https://github.com/python/mypy)
or [pyright](https://github.com/microsoft/pyright) to catch type problems in code early.

If you don't know what return type of API, just `Cmd+B` (PyCharm) or `F12` (VS Code) to
go to declaration, or hover over the function (API) to see well formatted docstring and
type hints.

- It accurately replicates the original API, preserving the exact parameters, function
  overloading, return types, and other specifications specified in the DaVinci Resolve
  API [README](READMEs).
- The docstrings are generated from the
  latest [DaVinci Resolve 18.5 Beta 5 README](READMEs/18.5b5_README.txt) and will be
  regularly updated.
- It functions as a development dependency or an interface. After development is
  finished, you can safely remove it without impacting the code's seamless operation in
  DaVinci Resolve, as it maintains the same signature as the original API.

## Get Started

### Prerequisites

...

# Similar Project

- [pybmd](https://github.com/WheheoHu/pybmd)

# Run Tests

```shell
pytest -v
```

By default, pytest captures the output produced by your tests and displays it only if
the test fails. However, when you
use `--capture=no` or `-s`, pytest allows the stdout and stderr to be displayed on the
console immediately, regardless
of the test result.

```shell
pytest -v -s
```

# After development using Dri

If your script intends to use outside DaVinci Resolve, then replace the import below

```python
from dri import Resolve

resolve = Resolve.resolve_init()
```

with:

```python
import DaVinciResolveScript as dvr_script

resolve = dvr_script.scriptapp("Resolve")
```

If your script intends to use inside DaVinci Resolve, replace with:

```python
resolve = bmd.scriptapp("Resolve")
```

## License

This project is licensed under the LGPLv3 License - see the [LICENSE](LICENSE) file for
details
