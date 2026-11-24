# Nitro 10X 12.0 Online — Landing Page

Versão **online e ao vivo** da LP do Nitro 10X 12.0 (03 a 05 de dezembro), ingresso **R$ 497** (12x de R$ 49,70).

## ✏️ Como editar pelo site do GitHub (sem instalar nada)

1. Abra o arquivo **`build_online.py`** aqui no repositório.
2. Clique no lápis ✏️ (**Edit this file**), no canto de cima à direita.
3. Ache o texto com **Ctrl+F** e troque **só o que está entre aspas** do lado direito.
   ```python
   rep("texto antigo da LP presencial", "texto novo da LP online")
   #                                     ^^^^^^^^^^^^^^^^^^^^^^^^ edite aqui
   ```
4. Clique em **Commit changes…** → **Commit changes**.
5. Espere ~1 minuto: o GitHub gera o **`online/index.html`** novo sozinho
   (acompanhe na aba **Actions** — bolinha verde ✅ = pronto, vermelha ❌ = deu erro).

> ⚠️ Não edite `online/index.html` direto: ele é refeito toda vez que o script roda e a sua mudança some.

**Se der ❌ vermelho:** quase sempre é uma aspa apagada sem querer ou um texto do lado
esquerdo que foi alterado (o lado esquerdo precisa ser idêntico ao da LP original).
Abra a execução em **Actions** para ver a mensagem `[ERRO] …`.

### Onde está cada coisa no `build_online.py`

| Procure por | O que muda |
|---|---|
| `CHECKOUT_ONLINE` | Link de pagamento do ingresso |
| `# ---------- seis motivos` | Os 6 motivos com foto |
| `12x de R$ 49,70` / `R$ 497` | Preço |
| `detail__perks` | Lista do que o ingresso inclui |
| `# ---------- FAQ` | Perguntas frequentes |
| `<style id="online">` | Ajustes de visual (cores, tamanhos) |

## Estrutura

| Pasta / arquivo | O que é |
|---|---|
| `online/index.html` + `online/assets/` | **A página pronta para publicar** (suba os dois juntos) |
| `build_online.py` | Script com todas as mudanças da versão online |
| `original/index.html` | Cópia da LP presencial (base de tudo) |
| `.github/workflows/gerar-pagina.yml` | Automação que roda o script a cada mudança |

## Editar no computador (opcional)

```
python -X utf8 build_online.py
python -m http.server 5510 --directory online
```

Abra http://localhost:5510

## Pendências

- [x] Link do checkout do ingresso online (`CHECKOUT_ONLINE` no topo de `build_online.py`)
- [ ] Confirmar a lista do que o ingresso inclui
