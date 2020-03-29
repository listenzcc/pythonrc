""" Useful decorators. """
import time
import threading


def d_timeit(Func):
    """ Timeit decorator. """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        f = Func(*args, **kwargs)
        print('Spent {} seconds.'.format(time.time() - start_time))
        return f
    return wrapper


class ThreadPool():
    def __init__(self):
        """ Pool is a list, simple and useful. """
        self.pool = []

    def refresh(self):
        """ Refresh thread pool. """
        self.pool = [t for t in self.pool if t.isAlive()]

    def append(self, t):
        """ Append new thread into the pool. """
        self.pool.append(t)
        self.refresh()

    def pprint(self):
        """ Print threads in the pool. """
        self.refresh()
        print(self.pool)


def d_thread(DefaultName='noname', DefaultThreadPool=None):
    """ New thread decorator. """
    def decorator(Func):
        def wrapper(*args, **kwargs):
            # Thread name
            Name = kwargs.get('ThreadName', DefaultName)
            # Start new thread
            t = threading.Thread(name=Name, target=Func, args=args, kwargs=kwargs)
            t.start()
            # Append into thread pool
            Pool = kwargs.get('ThreadPool', DefaultThreadPool)
            if Pool is not None:
                Pool.append(t)
            # Print thread started
            print(f'New thread started: {Name}.')
        return wrapper
    return decorator


if __name__ == '__main__':

    tp = ThreadPool()

    @d_timeit
    def add(a, b):
        time.sleep(a)
        print(a + b)

    f = (d_thread(DefaultThreadPool=tp))(add)
    f(3, 4)
    f(1, 2)

    while not input('>> ') == 'q':
        tp.pprint()

    print('ByeBye.')