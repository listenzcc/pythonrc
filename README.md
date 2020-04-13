# Custom Python profiles

Some useful python modules need custom setting.

Instead of setting them on every project, this project provides an easy way as .rc file in linux.

- [Custom Python profiles](#custom-python-profiles)
  - [How to use](#how-to-use)
  - [Logger module](#logger-module)

## How to use

Clone the repository to a path, like [this](~/.python).

Add the path into *$env:PYTHONPATH*, to make sure python app can find the customized modules.

*Note that, ipython and python may use different .rc profile.*

## Logger module

Custom setting of logging module.

*Known-issue: the logger is thread-save, but not process-save,
which means that default_logger file may suffer logging lost or mix-up,
when multi process conflict on writting logging file,
one solution is use different logging file when facing multi-process situation.*

```python
# Implement
from logger import default_logger as logger
```

Default settings
| Setting  | Value                                                |
| -------- | ---------------------------------------------------- |
| name     | root                                                 |
| encoding | utf-8                                                |
| pattern  | %(created)f - %(name)s - %(levelname)s - %(module)s:%(funcName)s - %message)s |
| filepath | root.log                                             |
| stream   | sys.stdout                                           |

Level settings
| Handler      | Level |
| ------------ | ----- |
| Stdout       | INFO  |
| Logging file | DEBUG |

