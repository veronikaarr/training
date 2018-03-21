from tasks import fib
from tasks import subpr
from random import randint

n = randint(30,40)
fib.delay(n)
subpr.delay()
