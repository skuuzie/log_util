from log_util import Log

# just like python's logging - if DEBUG level isn't set, debug loggings won't be seen
log = Log(name="MyApp", is_debug=True).get_logger()

# example to change color of a level
# log_util.level_color['DEBUG'] = log_util.COLOR_CYAN
# log_util.level_color['INFO'] = log_util.COLOR_HIGHLIGHTS

# print all color codes
# log_util.print_color_codes()

log.info('program start')
log.info('program reached the end\n')

test_var = [1,2,3,4,5]

log.debug('in test_debug')
log.debug('test_var is %s\n', test_var)

log.warning('server returned code %s', 500)
log.warning('subtraction of var_a and var_b is negative\n')

log.error("config.json is not found, exiting program")
log.error("unknown error!\n")

log.critical('not enough disk space to write, exiting program')
log.critical('not enough memory to read file, exiting program\n')