#           LOGGING
# tracking of program after it''s execution about it's error and status we have to keep it in
# some file called log file

#--------------while creating log file some levels are there:

# critical 50----- represents high attention needed for very serious problem
#  error 40---- represent a serious error
# warning 30 -----represent a warning message some caution is needed . it will alert the programmer
# info 20---represent a message with some important information
# debug 10----- represnt a message with debug information
# notset 0 ---- represnt that level is not set

import logging

logging.basicConfig(filename='log.txt',level=logging.DEBUG)
print("logging demo file")
logging.debug("this is debug message")
logging.warning("this is warning message")
logging.error("this is error meassage")
logging.critical("this is crtical message")
logging.info("this is info message")
print("end of program")


