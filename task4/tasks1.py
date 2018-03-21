import subprocess
import os
import psutil

cmd = subprocess.Popen(['ls', '-l'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out,error = cmd.communicate()
memory = out.splitlines()

for line in memory:
    print(line.decode('utf-8'))

"""CPU_Pct=str(round(float(os.popen('''grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }' ''').readline()),2))

print("CPU Usage = " + CPU_Pct)

tot_m, used_m, free_m = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])
print(tot_m, used_m, free_m)"""

o = psutil.cpu_times(True)

for lines in o:
    print(lines)