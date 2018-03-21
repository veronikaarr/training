'''from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def add(x, y):
    return x + y'''

from celery import Celery
import redis
import time
import subprocess

app = Celery('tasks')
app.config_from_object('celeryconfig')

# -----------------------------------------------------------------------------

def fib_slow(n):
    if n < 0:
        return 0
    if n in (0,1):        return 1
    return fib(n-1) + fib(n-2)

def fib_fast(n):
    s = subprocess.check_output(['./fib', str(n)])
    return s

def fib_to_file(n, filename):
    with open(filename, 'w') as outfile:
        cmd = ['./fib', str(n)]
        subprocess.call(cmd, stdout=outfile)
        sys.stderr.write('Wrote ' + outfile.name + '\n')
    return True

# -----------------------------------------------------------------------------

@app.task
def add(x, y):
    if True:
        time.sleep(10)
    return x + y

@app.task
def fib(n):
    f = fib_fast(n)
    if True:
        time.sleep(10)
    if True:
        r = redis.Redis('localhost')
        r.publish('tasks:all', f)
    return n
