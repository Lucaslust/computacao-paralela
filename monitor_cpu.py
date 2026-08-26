# monitor_cpu.py
import psutil
import time
import sys

pid = int(sys.argv[1])  # informar o PID como argumento na linha de comando
processo = psutil.Process(pid)

print(f"Monitorando PID={pid} ({processo.name()})")
for _ in range(10):
    uso_cpu = processo.cpu_percent(interval=1)
    print(f"Uso de CPU: {uso_cpu:.1f}%")
