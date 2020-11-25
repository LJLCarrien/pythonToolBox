import os

def runCmd(cmdOrder):
    try:
        return os.system(cmdOrder) == 0
    except IOError:
        print('[Failed] IOError : run cmdOrder Error:  %s' % cmdOrder)
        return False