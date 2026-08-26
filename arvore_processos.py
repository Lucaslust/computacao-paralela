import psutil
import os

def imprimir_cadeia_ancestrais(pid):
    cadeia = []
    try:
        processo = psutil.Process(pid)
        while processo is not None:
            cadeia.append(f"{processo.name()} (PID={processo.pid})")
            processo = processo.parent()
    except psutil.NoSuchProcess:
        pass
    # Imprime da raiz até o processo original
    print(" -> ".join(reversed(cadeia)))

pid_atual = os.getpid()
imprimir_cadeia_ancestrais(pid_atual)
