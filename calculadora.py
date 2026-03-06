import time
from datetime import datetime

# Exibe o horário atual e atualiza a cada 1 segundo
# \r faz o cursor voltar pro início da linha (sobrescreve)
# end="" evita pular linha
# flush=True força aparecer na tela na hora

while True:
    print("\r" + datetime.now().strftime("%H:%M:%S"), end="", flush=True)
    time.sleep(1)
