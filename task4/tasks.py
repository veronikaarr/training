#celery -A tasks worker --loglevel=info
#python3 tasks1.py

from celery import Celery
import subprocess
import psutil

app = Celery('tasks')
file = open('log.txt', 'w')

# -----------------------------------------------------------------------------
@app.task
def fib_slow(n):
    if n < 0:
        return 0
    if n in (0,1):        return 1
    return fib(n-1) + fib(n-2)

# -----------------------------------------------------------------------------

@app.task
def subpr():
    cmd = subprocess.Popen(['ls', '-l'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out,error = cmd.communicate()
    memory = out.splitlines()

    for line in memory:
        file.write(str(line.decode('utf-8')) + '\n')
        #print(line.decode('utf-8'))

    o = psutil.cpu_times(True)

    for lines in o:
        file.write(str(lines) + '\n')
        #print(lines)

@app.task
def fib(n):
    f = fib_slow(n)
    subpr()
    print(f)
    return f

