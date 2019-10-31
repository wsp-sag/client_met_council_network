# ScriptManager.py
# very primitive attempt at a python-side controller
# input is command line for now
# expecting one or more python file names (modules) 
# each representing configuration information for a model component

import os
import sys
import ModelStructure
import logging
import logging.handlers
import time
import subprocess
import shlex

LOG_FILE = r"logs\tourcastPython.log"
LOG_FILESIZE = 40000000
LOG_LEVEL = logging.INFO

log = logging.getLogger("ScriptManager")
log.setLevel(logging.INFO)
loghandler = logging.handlers.RotatingFileHandler(
    LOG_FILE, maxBytes=LOG_FILESIZE, backupCount=10)
log.addHandler(loghandler)


now = time.ctime(time.time())
print "arg count = {0}".format(sys.argv.count(0)) 
log.info("ScriptManager.py started {0}".format(now))
log.info("ScriptManager.py arguments {0}".format(sys.argv))


def handle_switch(s):
    if s == 'help' or s == '?':
        print_help()
        return

    """ switch is form option:value """
    opt, val = s.split(':')
    if opt == "loglevel":
        set_log_level(val)
    else: 
        pass

def set_log_level(s):
    if s == "INFO":
        log.setLevel(logging.INFO)
    elif s == "DEBUG":
        log.setLevel(logging.DEBUG)
    elif s == "WARNING":
        log.setLevel(logging.WARNING)
    elif s == "CRITICAL":
        log.setLevel(logging.CRITICAL)
    elif s == "ERROR":
        log.setLevel(logging.ERROR)

def print_help():
    print "command line example (don't append .py to component names):"
    print "python ScriptManager [/help][/?] [/loglevel:DEBUG|INFO|WARNING|ERROR|CRITICAL] componentA componentB"
    
if sys.argv.count == 1:
    print_help()
    quit()

for mod in sys.argv[1:]:
    if mod.startswith('/'):
        handle_switch(mod.strip("/"))
        continue
    log.info("loading configuration for {0}".format(mod))
    ms = ModelStructure.ModelStructure(mod)
    log.info("before ModelStructure.load_config()")
    ms.load_config()
    log.info("before ModelStructure.dump()")
    log.debug(ms.dump())
    configDest = mod
    log.info("request export of {0} configuration into {1}".format(mod, configDest))
    configFilename = ms.export_json(configDest)
    log.info("Component {0} configuration loaded into {1}".format(mod, configFilename))
          



