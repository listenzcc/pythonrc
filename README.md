# Custom Python profiles

Some useful python modules need custom setting.

Instead of setting them on every project, this project provides an easy way as .rc file in linux.

- [Custom Python profiles](#custom-python-profiles)
  - [How to use](#how-to-use)
  - [Logger module](#logger-module)

## How to use

Clone the repository to a path, like [this](~/.python).

Add the path into *$env:PYTHONPATH*, to make sure python app can find the customized modules.

## Logger module

Custom setting of logging module.

```python
# Implement
from logger import default_logger as logger
```

Default settings
| Setting  | Value                                                |
| -------- | ---------------------------------------------------- |
| name     | root                                                 |
| encoding | utf-8                                                |
| pattern  | %(asctime)s - %(name)s - %(levelname)s - %(message)s |
| filepath | root.log                                             |
| stream   | sys.stdout                                           |

Level settings
| Handler      | Level |
| ------------ | ----- |
| Stdout       | INFO  |
| Logging file | DEBUG |

