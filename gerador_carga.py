# gerador_carga.py — roda até ser interrompido com Ctrl+C
import os

print(f"Gerando carga de CPU. PID deste processo: {os.getpid()}")
print("Pressione Ctrl+C para interromper.")

x = 0
while True:
    x += 1
