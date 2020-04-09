from datetime import datetime
import functools


def monitor(method):
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        print('-->  %s.%s' % (self.__module__, method.__name__))
        start = datetime.now()
        rsp = method(self, *args, **kwargs)
        end = datetime.now()
        usedmsec = (end - start).seconds * 1000 + (end - start).microseconds / 1000.0
        print('<--  %s.%s used: %0.2f ms' % (self.__module__, method.__name__, usedmsec))
        return rsp
    return wrapper


def monitor_function(method):
    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        start = datetime.now()
        rsp = method(*args, **kwargs)
        end = datetime.now()
        print(f'<-- {method.__name__} used: {(end - start)}')
        return rsp
    return wrapper


@monitor_function
def add(a, b):
    return a+b


add(2,3)
print(add.__name__)
