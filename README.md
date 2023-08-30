# log_util

just a single python file utility module for logging with colorization feature. 

---

it's basically python's very own `logging` with colorization and tidier (my preference on) formatting

**basic usage**
```py
import log_util

log = log_util.Log(name="MyApp", is_debug=True).get_logger()

log.info('info message')
log.debug('debug message')
log.warning('warning message')
log.error('error message')
log.critical('critical message')
```

**output example**
```
[2020-20-20 20:20:20,200] [MyApp] INFO: program is starting...
[2020-20-20 20:20:20,200] [MyApp] ERROR: an external error has occured! exiting program...
```

--- 

if you want to customize the formatting and color output, you can manually make changes in `log_util.py`, it also has `print_color_codes` function to print all ANSI color codes and you can use them however you like it

everything should be demonstrated in `examples.py`