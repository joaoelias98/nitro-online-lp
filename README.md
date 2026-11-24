# Nitro 10X 12.0 Online — Landing Page

Versão **online e ao vivo** da LP do Nitro 10X 12.0 (03 a 05 de dezembro), ingresso **R$ 497** (12x de R$ 49,70).

## Estrutura

| Pasta / arquivo | O que é |
|---|---|
| `online/index.html` + `online/assets/` | **A página pronta para publicar** (suba os dois juntos) |
| `build_online.py` | Script que gera `online/index.html` a partir da LP presencial |
| `original/index.html` | Cópia da LP presencial (base de tudo) |

## Como editar

Os textos e ajustes da versão online ficam todos em `build_online.py`.
Edite lá e gere a página de novo:

```
python -X utf8 build_online.py
```

> Não edite `online/index.html` direto: ele é sobrescrito toda vez que o script roda.

## Ver localmente

```
python -m http.server 5510 --directory online
```

Abra http://localhost:5510

## Pendências

- [ ] Link do checkout do ingresso online: trocar `CHECKOUT_ONLINE` no topo de `build_online.py`
