import psutil
import os

pid = os.getpid()  # PID do próprio script Python em execução
# Para consultar outro processo, troque por: pid = <PID_desejado>

processo = psutil.Process(pid)
print(f"Processo PID={pid} — Nome: {processo.name()}")
print(f"Número de threads: {processo.num_threads()}")
print("\nDetalhe de cada thread (id, tempo de usuário, tempo de sistema):")
for t in processo.threads():
    print(f" Thread ID={t.id} tempo_usuario={t.user_time:.4f}s tempo_sistema={t.system_time:.4f}s")
