# Módulo 1 - Programas, Processos e Threads em um PC

Atividades práticas da disciplina de Programação Paralela e Concorrente.

## Instalação

### 1. Instalar Python
Se ainda não tiver o Python instalado:
1. Acesse https://www.python.org/downloads/
2. Baixe a versão mais recente
3. **IMPORTANTE**: Marque a opção "Add python.exe to PATH" durante a instalação

### 2. Instalar a biblioteca psutil
Abra o PowerShell ou Prompt de Comando e execute:
```bash
pip install psutil
```

## Como usar os scripts

### Atividade 1.1 - Programa vs. Processo

**Objetivo**: Comprovar que abrir várias vezes o mesmo programa cria vários processos independentes.

**Passo a passo**:
1. Abra o Bloco de Notas (notepad) **3 vezes** manualmente
2. Execute o script:
   ```bash
   python listar_processos.py
   ```
3. Anote os PIDs de cada processo
4. Feche uma janela do Bloco de Notas
5. Execute novamente e confirme que um PID desapareceu

**Dica**: Para buscar outro programa, edite o arquivo `listar_processos.py` e mude a variável `nome_alvo`.

---

### Atividade 1.2 - Explorando threads de um processo

**Objetivo**: Verificar que um único processo pode conter múltiplas threads internas.

**Passo a passo**:
1. Execute o script:
   ```bash
   python threads_do_processo.py
   ```
2. O script mostra quantas threads ele próprio possui
3. Para ver threads de outro processo, edite o arquivo e mude `pid = <PID_desejado>`
4. Anote o número de threads

**Dica**: Processos como navegadores (chrome.exe, firefox.exe) têm muito mais threads que um script Python simples.

---

### Atividade 1.3 - Árvore de processos

**Objetivo**: Visualizar a hierarquia pai-filho de processos.

**Passo a passo**:
1. Execute o script:
   ```bash
   python arvore_processos.py
   ```
2. O script mostra a cadeia de processos desde a raiz até ele mesmo
3. Desenhe essa cadeia no relatório

---

### Atividade 1.4 - Monitoramento em tempo real com carga de CPU

**Objetivo**: Observar visualmente o efeito de um processo consumindo CPU.

**Passo a passo**:

1. **Terminal 1** - Abra um PowerShell e execute:
   ```bash
   python gerador_carga.py
   ```
   Anote o PID que aparece na tela (por exemplo: 12345)

2. **Terminal 2** - Abra outro PowerShell e execute (substitua 12345 pelo PID anotado):
   ```bash
   python monitor_cpu.py 12345
   ```

3. Observe o uso de CPU subir para próximo de 100%

4. Para parar, volte ao Terminal 1 e pressione `Ctrl+C`

**Alternativa**: Use o Gerenciador de Tarefas do Windows (Ctrl+Shift+Esc) para ver o consumo de CPU visualmente.

---

## Estrutura dos arquivos

```
Computacao paralela/
├── listar_processos.py      # Atividade 1.1
├── threads_do_processo.py   # Atividade 1.2
├── arvore_processos.py      # Atividade 1.3
├── gerador_carga.py         # Atividade 1.4 (gera carga)
├── monitor_cpu.py           # Atividade 1.4 (monitora)
├── README.md                # Este arquivo
└── relatorio.tex            # Template do relatório em LaTeX
```

## Questões para o relatório

Após executar todas as atividades, responda no relatório:

1. Qual a diferença entre PID e PPID? Ilustre com um exemplo observado na Atividade 1.3.
2. Ao abrir três instâncias do mesmo programa, quantos PIDs você observou? Eles compartilham memória entre si?
3. Quantas threads o processo analisado na Atividade 1.2 possuía? Isso foi surpreendente?
4. Os resultados obtidos pelo script Python (psutil) bateram com os resultados da ferramenta nativa (Gerenciador de Tarefas)?
5. Qual ferramenta você usou e por quê? Alguma dificuldade encontrada?
6. Com base na experiência prática, escreva com suas próprias palavras a diferença entre processo e thread.

---

## Dicas

- Use o **Gerenciador de Tarefas** (Ctrl+Shift+Esc) para visualizar processos e threads graficamente
- Na aba "Detalhes" do Gerenciador de Tarefas, você pode ver os PIDs
- Para ver threads no Gerenciador, baixe o **Process Explorer** (gratuito da Microsoft): https://learn.microsoft.com/sysinternals/downloads/process-explorer

---

**Boa prática!**
