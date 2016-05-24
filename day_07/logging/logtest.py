# level = DEBUG,        (low)      [fine-grained debugging]
#         INFO,
#         WARNING, (default level)
#         ERROR,
#         CRITICAL      (high)     [system going down]

# filemode = 'a' (append)    (default filemode)
#            'w' (overWrite)
import logging
# some simple setups
#logging.basicConfig(filename="log.txt")
logging.basicConfig(filename='log.txt',
                    filemode='w',
                    level=logging.DEBUG)

def simple(x,y):
    logging.info('start simple()')
    logging.warning('x:%d y:%d', x, y)
    logging.info('end simple()')
simple(3,5)




def divide(x,y):
    logging.info('start divide()')
    logging.debug('x:%d y:%d' % (x,y))
    try:
        res = x/y
        return res
    except ZeroDivisionError:
        logging.critical("couldn't divide by zero")
        raise SystemExit
    finally:
        logging.info('end divide()')
# divide(8,2)
