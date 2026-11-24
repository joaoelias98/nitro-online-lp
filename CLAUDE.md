# Nitro 10X 12.0 Online — LP

Landing page da versão **online e ao vivo** do Nitro 10X 12.0 (03 a 05/12), ingresso único de **R$ 497**
(12x de R$ 49,70), ancorado em "De R$ 997, 50% OFF".
Checkout: `CHECKOUT_ONLINE` no topo do script; no JS a chave é `'Online ao vivo'` (o valor de `data-lead-tier`). Quem pede as mudanças é o time de marketing, em português e sem termos técnicos:
responda em português, explique o que mudou em linguagem simples e mostre o resultado.

## Como o projeto funciona (leia antes de editar)

- `original/index.html` é a cópia da LP **presencial** (Astro, minificada). **Nunca edite.**
- `build_online.py` aplica todas as mudanças da versão online sobre o original e gera `online/index.html`.
  **Toda edição é feita aqui.**
- `online/index.html` é **gerado**. Não edite à mão: some na próxima geração.
- `online/assets/` tem as imagens (webp). Os caminhos são relativos (`assets/...`).

Depois de qualquer mudança no script, gere de novo e confira:

```
python -X utf8 build_online.py
```

O aviso `[aviso] ainda aparece 'na sala' 1x` é esperado (é um texto novo, intencional).
Um `[ERRO] ...` significa que um trecho de busca não bate mais com o original: corrija o trecho.

## Regras do script

- `rep(antigo, novo)` troca texto exato e **falha** se não achar; `rx(regex, novo)` idem com regex.
- O HTML original tem atributos `data-astro-cid-*` nas tags: ao trocar algo com tag, use regex
  tolerante (`<span[^>]*>`) ou troque só o texto. Esses atributos são usados pelo CSS: não remova.
- Ajustes de visual entram nos blocos `<style id="online">` e `<style id="logo-online">` do script.
  Para vencer o CSS original no celular use `:not(#_)` (é o padrão já usado no projeto).
- Breakpoints do original: celular/tablet `max-width:999px`, PC `min-width:1000px`.
- O arquivo é salvo com `newline="\n"` de propósito (a mesma saída no Windows e no GitHub Actions).

## Decisões já tomadas (não desfazer sem pedirem)

- Ingresso único "Online", com o **visual Diamond** (verde), e botão no estilo padrão `btn--primary`.
- Logo com a tarja **ONLINE**: ao lado da logo no PC, embaixo e centralizada no celular.
- "Ao vivo" sinalizado só com a **bolinha verde piscando** (`.live-dot`). **Sem selo vermelho.**
- Na barra verde do topo a bolinha é escura (senão some no fundo verde).
- Celular: o KV do topo é mais baixo e sobe (`object-position:50% 72%`), com o degradê escuro do topo
  reduzido para não sombrear os rostos. As linhas decorativas `.hb-lines` ficam escondidas no hero.
- Foto do Pyero na seção do mentor: `online/assets/pyero-palco-{420,640,880,1200}.webp`.
  Foto nova: converter para webp nesses 4 tamanhos (Pillow, qualidade ~78) e usar `srcset`.
- O lead vai para o mesmo webhook do n8n com `ingresso: "Online ao vivo"`.
  O pixel da Meta só dispara no domínio nitro10x.com.br (não suja no preview).

## Pendências

- O que o ingresso inclui (lista `detail__perks`) foi escrito com base no ingresso Gold: confirmar com o time.

## Conferir antes de entregar

1. Gere a página e abra `online/index.html` (ou `python -m http.server 5510 --directory online`).
2. Veja no **PC (1280px+)** e no **celular (375px)**: sem rolagem para os lados, nada sobrepondo os rostos.
3. Botão do ingresso abre o formulário com "Ingresso Online ao vivo". **Não envie o formulário**:
   ele manda lead de verdade para o webhook.

## Git

- Commits em português, curtos, dizendo o que mudou na página.
- O GitHub Actions (`.github/workflows/gerar-pagina.yml`) também gera a página a cada push no script,
  então mesmo uma edição feita pelo site do GitHub sai atualizada.
- Antes de editar, puxe a versão mais nova (`git pull`): outras pessoas também editam.
