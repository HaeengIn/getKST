# getKST
A Python package that returns datetime values ​​for the Asia/Seoul region.

[![PyPI version](https://img.shields.io/pypi/v/getKST.svg)](https://pypi.org/project/getKST/)
[![Python versions](https://img.shields.io/pypi/pyversions/getKST.svg)](https://pypi.org/project/getKST/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Installation
### Prerequisites
- Python (>=3.9)

### Install via pip
```bash
pip install getKST
```
### Install via  uv
```bash
uv add getKST
```

## Usage
Note: Default format of **getKST** is `%Y-%m-%d %H:%M:%S` as a string.

`getKST()` always converts to Asia/Seoul time internally before formatting, so the result is identical no matter what timezone the host machine or server is set to (UTC, EST, JST, etc.).

- Basic Usage
    ```python
    from getKST import getKST

    now = getKST()
    print(now)
    ```
- Using other formats
    ```python
    from getKST import getKST

    now = getKST("%Y/%m/%d")  # Year/Month/Date
    now = getKST("%H-%M-%S")  # Hour-Minute-Second
    ```
- Converting an existing datetime
    ```python
    from datetime import datetime, timezone
    from getKST import getKST

    utc_now = datetime.now(tz=timezone.utc)
    print(getKST(dt=utc_now))
    ```
All Python datetime formats are supported.

## License
[MIT](./LICENSE)