# !user/bin/ev/python3
# -*- coding: utf-8 -*-

import math

Tc = 27
Ts = 221
Tw = 514

lamda = 1/Tc
nu = 1/Ts
a = lamda/nu
n = 10
P0 = 0

Pn = [(math.pow(a, x) / math.factorial(x)) for x in range(0, n)]
print(Pn)

P0 = list(map(lambda y: (1 / sum((math.pow(a, x) / math.factorial(x)) for x in range(0, y))), range(1, n)))
print(P0)