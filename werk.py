#!/usr/bin/env python

import os
logfile = os.environ['HOME'] + '/.werklog'
import logging
import json
import pydoc
import sys

FORMAT = '%(asctime)-15s: %(message)s'
logging.basicConfig(filemode='a',format=FORMAT, filename=logfile)
console = logging.StreamHandler()
formatter = logging.Formatter(FORMAT)
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)                                 


def log(proj,msg):
    """ message proj msg"""  
    logging.warning("%s" % json.dumps(dict(proj=proj, msg=msg)))
    
def start(proj):
    log(proj,'started')
    
def stop(proj):
    log(proj,'stopped')


def status(proj):
    for x in open(logfile):
        if proj in x:
            print x.strip()


cmds = ['log','start','stop']
def h(cmd=None):
    if cmd:
        L = [cmd,]
    else:
        L = cmds[:]

    for x in L:
        print x
        print pydoc.getdoc(eval(x))

def run(*args):
    if not args:
        args = sys.argv[1:]
        if not args:
            args = ['h']
    
    f = eval(args[0])
    f(*args[1:])
    
if __name__ == '__main__':
    import sys
    print sys.argv
    run(*sys.argv[1:])
