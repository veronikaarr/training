# !user/bin/ev/python3
# -*- coding: utf-8 -*-

import math
import matplotlib.pyplot as plt
import numpy as np

Tc = 27
Ts = 221
Tw = 523

'''Первый пункт'''

lamda = 1/Tc
nu = 1/Ts
a = lamda/nu
n = 15
Potk = list()
Pobsl = list()
nsr = list()

Pn = [(math.pow(a, x) / math.factorial(x)) for x in range(0, n)]

Po = list(map(lambda y: (1 / sum(Pn[0:y])), range(1, n+1)))

for x in range(0, n):
    Potk.append(Pn[x] * Po[x])
    Pobsl.append(1 - Potk[x])
    if x != 0:
        nsr.append(a*Pobsl[x]/x)

Potk = list(map(lambda x:round(x,3), Potk))
nsr = list(map(lambda x:round(x,3), nsr))

x = np.linspace(1, n, 0.1)
z = [x for x in range(1,n)]
plt.plot(z, Potk[1:n], z, nsr[0:n], color='red', marker='o', linestyle='--', markerfacecolor='blue')
for i,j in zip(z,Potk):
    plt.text(i, j, str(j))
for w,e in zip(z,nsr):
    plt.text(w, e, str(e))
#plt.show()


'''Второй пункт'''

Po_promej = [(math.pow(a, x) / math.factorial(x)) for x in range(0, n)]

m = 15

#for i

Po_2 = list(map(lambda x: (1 / (sum(Po_promej[0:n]) + (math.pow(a, n + 1) / math.factorial(n) * (n - a)) *
                                  (1 - (math.pow((a / n), x))))), range(1, m + 1)))

Potk_2 = list(map(lambda y: ((math.pow(a, (n+y)) * Po_2[y-1]) / (math.factorial(n) * math.pow(n,y))), range(1, m + 1)))

q = list(map(lambda z: (a * (1 - (math.pow(a, (n+z)) * Po_2[z-1]) / (math.factorial(n) * math.pow(n,z))) / n), range(1, m+1)
             ))

Loh_promej = [ x * Potk_2[x-1] for x in range(1, m+1)]

Loh = list(map(lambda q_: (sum(Loh_promej[0:q_])), range(1, m+1)))

S = list(map(lambda e: Loh[e-1] / e, range(1,m+1)))

Tsr = list(map(lambda r: (Loh[r] / lamda), range(0, m)))

print('Po_2 = {0} \n'.format(Po_2))
print('Potk_2 = {0} \n'.format(Potk_2))
print('q = {0} \n'.format(q))
print('Loh = {0} \n'.format(Loh))
print('S = {0} \n'.format(S))
print('Tsr = {0} \n'.format(Tsr))

'''Третий пункт'''

Po_promej_3 = [(math.pow(a, x) / math.factorial(x)) for x in range(0, n)]

m = 15

Po_3 = list(map(lambda x: (1 / (sum(Po_promej_3[0:n]) + (math.pow(a, n + 1) / math.factorial(n) * (n - a)))), range(1, m + 1)))

print('Po_3 = {} \n'.format(Po_3))

