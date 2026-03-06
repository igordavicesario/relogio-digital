# Relógio Digital em Tempo Real

Aplicação Python que exibe o horário atual no terminal, atualizado a cada segundo.

## O que aprendi

- Uso do módulo `datetime` para obter a hora atual
- Formatação de strings com `strftime`
- Loop infinito com `while True`
- Uso de `\r`, `end=""` e `flush=True` para sobrescrever a linha no terminal
- Tratamento de interrupção com `KeyboardInterrupt`

## Como executar

```bash
python relogio.py
```

Você pode escolher entre 3 modos ao iniciar o programa.

## Conceitos utilizados

| Conceito | Descrição |
|---|---|
| `datetime.now()` | Retorna data e hora atual |
| `.strftime("%H:%M:%S")` | Formata hora:minuto:segundo |
| `time.sleep(1)` | Pausa a execução por 1 segundo |
| `\r` | Retorna o cursor pro início da linha |
| `flush=True` | Força a exibição imediata no terminal |

## Estrutura

```
relogio-digital/
│
└── relogio.py     # código principal com 3 modos
```

---
Desenvolvido por [Igor Davi](https://github.com/igordavicesario) • FIAP Engenharia de Software
