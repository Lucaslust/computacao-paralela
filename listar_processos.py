import psutil

# Troque pelo nome do processo do seu aplicativo:
# Linux: "gedit" | Windows: "notepad.exe"
nome_alvo = "notepad.exe"

print(f"Processos encontrados para '{nome_alvo}':")
for processo in psutil.process_iter(["pid", "name", "ppid"]):
    if nome_alvo.lower() in processo.info["name"].lower():
        print(f" PID={processo.info['pid']} PPID={processo.info['ppid']} Nome={processo.info['name']}")
