# Gera online/index.html a partir de original/index.html (LP presencial do Nitro 10X 12.0).
# Mantém todo o design/CSS/JS originais e troca só o conteúdo para a versão ONLINE (ingresso R$ 497).
# Rodar:  python -X utf8 build_online.py
import re, pathlib

ROOT = pathlib.Path(__file__).parent
s = (ROOT / "original" / "index.html").read_text(encoding="utf-8")

# >>> COLE AQUI o link de checkout do ingresso online (R$ 497) <<<
CHECKOUT_ONLINE = "https://pay.nitro10x.com.br/pay/nitro-10x-120-online-site"

def rep(old, new, count=None):
    """Troca exata; falha se o trecho não existir (evita troca silenciosa errada)."""
    global s
    n = s.count(old)
    if n == 0 or (count is not None and n != count):
        raise SystemExit(f"[ERRO] esperado {count or '>=1'} ocorrência(s), achei {n}: {old[:80]!r}")
    s = s.replace(old, new)

def rx(pattern, new, flags=re.S):
    global s
    s2, n = re.subn(pattern, new, s, flags=flags)
    if n == 0:
        raise SystemExit(f"[ERRO] regex sem match: {pattern[:80]!r}")
    s = s2

# ---------- assets locais ----------
s = s.replace("/nitro10x_dez26/lp/", "assets/")

# ---------- SEO ----------
rep("<title>Nitro 10X 12.0 — 03 a 05 de dezembro em Alphaville</title>",
    "<title>Nitro 10X 12.0 Online — 03 a 05 de dezembro, ao vivo</title>")
rep('content="Nitro 10X 12.0 — 03 a 05 de dezembro em Alphaville"',
    'content="Nitro 10X 12.0 Online — 03 a 05 de dezembro, ao vivo"')
rep("Imersão presencial para donos e sócios de empresa, de 03 a 05/12 em Alphaville, Barueri/SP.",
    "Imersão online e ao vivo para donos e sócios de empresa, de 03 a 05/12. Assista de onde estiver por R$ 497.", 2)

# ---------- barra do topo + hero ----------
rep('<span>Alphaville · Barueri/SP</span><i class="hide-sm"></i><span class="hide-sm">Imersão presencial</span>',
    '<span class="live-badge"><i></i>Ao vivo</span><i class="hide-sm"></i><span>Online</span><i class="hide-sm"></i><span class="hide-sm">Transmissão em tempo real</span>')
# selo AO VIVO acima do título do hero
rx(r'(<div class="hero__copy"[^>]*>)', r'\1<span class="live-badge"><i></i>Ao vivo · 03 a 05 de dezembro · online</span>')
rx(r'(<dt[^>]*>)Local(</dt> <dd[^>]*>)Alphaville · Barueri/SP(</dd> </div> <div[^>]*> <dt[^>]*>Impacto)',
   r'\1Formato\2<span class="live-dot"></span>Online · ao vivo\3')
rx(r'Agora é a\s+sua vez de trocar o medo do cenário', 'Agora você assiste <strong>ao vivo</strong>, de onde estiver, e troca o medo do cenário')
rx(r'(<a href="#bilhetes" class="btn btn--primary"[^>]*>)Garantir meu ingresso(</a>)', r'\1Quero assistir ao vivo\2')

# ---------- seis motivos (eram todos sobre estar fisicamente na sala) ----------
rep("Seis motivos para estar nesta sala", "Seis motivos para estar ao vivo")
rep("Encurte o caminho até a venda.", "Aprenda sem sair da sua cidade.")
rep("Em venda complexa ou de tíquete alto, ninguém fecha sem confiar. Uma conversa olho no olho pode adiantar o que dezenas de e-mails e chamadas não resolveram.",
    "Sem passagem, sem hotel e sem dias longe da empresa. Você recebe o mesmo conteúdo do palco, ao vivo, do seu escritório ou da sua casa.")
rep("Fale direto com quem decide.", "Veja como pensam os donos de empresa.")
rep("Sem secretária, sem filtro de e-mail e sem &quot;vou levar para o dono&quot;. Aqui, a conversa acontece de empresário para empresário.",
    "Nada de teoria de quem nunca empreendeu. O conteúdo é de empresário para empresário, com casos reais de quem já passou pelo que você está vivendo.")
rep("Encontre muitos contatos em um só lugar.", "Assista com o seu time e o seu sócio.")
rep("Em vez de viajar para visitar empresários em vários estados, você conhece pessoas de diferentes mercados no mesmo evento.",
    "Coloque a transmissão na sala de reunião e alinhe as decisões com quem executa. Todo mundo sai com a mesma visão para 2027.")
rep("Descubra o que o mercado está fazendo.", "Descubra o que o mercado está fazendo.")
rep("Nas conversas de bastidores, você entende como outros donos estão lidando com preço, equipe e crescimento.",
    "Você entende como outros donos estão lidando com preço, equipe, nova jornada e crescimento, antes que o cenário aperte.")
rep("Amplie sua rede de fornecedores e parceiros.", "Aplique enquanto assiste.")
rep("Novas opções aumentam o seu poder de negociação. E três dias com um sócio ou parceiro abrem conversas que não cabem em uma reunião.",
    "Pause entre os blocos, anote e já leve para a empresa. Três dias com a cabeça no plano valem mais do que meses apagando incêndio.")
rep("Teste suas ideias e fortaleça sua marca.", "Pague uma fração do presencial.")
rep("Apresente sua oferta, ouça reações sinceras e seja visto entre empresários que estão investindo no próximo passo.",
    "O mesmo método, os mesmos 3 dias e o mesmo Pyero, por R$ 497. É o jeito mais acessível de viver o Nitro 10X em 2026.")
rx(r"<strong([^>]*)>Se uma conversa virar um cliente, um fornecedor melhor ou uma parceria, o ingresso\s+pode se pagar\.</strong> Nenhum resultado é garantido, mas essa conversa não acontece se você\s+não estiver na sala\.",
   r"<strong\1>Se uma única decisão certa vier destes 3 dias, o ingresso se paga.</strong> Nenhum resultado é garantido, mas essa decisão não acontece se você não estiver ao vivo.")
rep("Novos contatos para gerar clientes, parcerias e oportunidades.",
    "Ideias e referências de outros empresários para gerar clientes e oportunidades.")

# ---------- seção de ingressos: 1 ingresso online ----------
rep("Escolha a melhor experiência para aproveitar os três dias. Cada participante precisa do\n        próprio ingresso; venha com o seu sócio ou cônjuge.",
    "Um único ingresso, com acesso ao vivo aos três dias de imersão. Assista de onde estiver,\n        pelo celular ou computador.")
# remove o mapa da plenária
rx(r'<div class="seatmap" id="mapa".*?(?=<div id="bilhetes")', "")
# remove Diamond e Platinum (fica só um card, baseado no Gold)
rx(r'<article id="ingresso-diamond".*?(?=<article id="ingresso-gold")', "")
# radios / abas do celular
rx(r'<input type="radio" name="tier" id="tier-diamond"[^>]*>', "")
rx(r'<input type="radio" name="tier" id="tier-platinum"[^>]*>', "")
rx(r'(<input type="radio" name="tier" id="tier-gold" class="sel__input")', r'\1 checked')
rx(r'<div class="tabs"[^>]*>.*?</div>', "")
# o card
# visual Diamond (verde) no lugar do Gold
rep('<article id="ingresso-gold" class="tier tier--gold tier--featured"',
    '<article id="ingresso-online" class="tier tier--diamond"')
rep('id="tier-gold" class="sel__input" checked aria-label="Ingresso Gold"',
    'id="tier-diamond" class="sel__input" checked aria-label="Ingresso Online ao vivo"')
rep('class="card card--gold"', 'class="card card--diamond"')
rep('class="detail detail--gold"', 'class="detail detail--diamond"')
# botão do ingresso no estilo padrão do site (o mesmo verde do hero)
rep('btn btn--block btn--holo btn--holo-gold detail__cta', 'btn btn--block btn--primary detail__cta')
rx(r'(<span class="card__kicker"[^>]*>)Ingresso(</span> <span class="card__name"[^>]*>)Gold(</span>)',
   r'\1Ingresso online\2Ao vivo\3')
rx(r'(<dt[^>]*>)Local(</dt> <dd[^>]*>)Alphaville · Barueri/SP(</dd>)', r'\1Formato\2<span class="live-dot"></span>Online · ao vivo\3')
rx(r'Ingresso Gold (<span[^>]*>)Para viver os 3 dias(</span>)',
   r'<span class="live-badge"><i></i>Ao vivo</span> Ingresso Online \1Os 3 dias transmitidos ao vivo, direto do palco do Nitro 10X\2')
rx(r'<div class="price"([^>]*)>.*?</div>',
   r'<div class="price"\1><p class="price__from">De <s>R$ 997</s><span class="price__off">50% OFF</span></p>'
   r'<p class="price__now"><span class="sr-only">por </span>12x de R$ 49,70</p>'
   r'<p class="price__cash">ou R$ 497 à vista</p></div>')
rx(r'(<ul class="detail__perks"[^>]*>).*?(</ul>)', lambda m: m.group(1) + "".join(
    f'<li class="perk" data-astro-cid-yktxaogb>{p}</li>' for p in [
        "<span><strong>Transmissão AO VIVO</strong> dos 3 dias (03, 04 e 05/12)</span>",
        "Direto do palco, em tempo real, junto com a plateia presencial",
        "Assista pelo celular, tablet ou computador",
        "Imersão com sistema de planejamento estratégico para 2027",
        "Gravação do 10X Private",
        "Material complementar digital pós-evento",
    ]) + m.group(2))
rep('data-lead-tier="Gold" aria-label="Garantir ingresso Gold"',
    'data-lead-tier="Online ao vivo" aria-label="Garantir ingresso Online ao vivo"')
rx(r'\n\s*Garantir Gold </a>', "\nQuero assistir ao vivo </a>")

# CSS: um card centralizado + selo "AO VIVO" pulsando
rep("</head>", """<style id="online">
#bilhetes .tiers{grid-template-columns:minmax(0,540px)!important;justify-content:center}
#bilhetes .tiers__x{display:none!important}
#bilhetes .tier--diamond{display:flex}
.live-badge{display:inline-flex;align-items:center;gap:.45em;padding:.28em .7em .28em .6em;border-radius:4px;
  background:#e5323b;color:#fff;font-family:var(--font-display);font-weight:800;font-size:.72rem;letter-spacing:.14em;
  text-transform:uppercase;line-height:1;vertical-align:middle;box-shadow:0 0 18px rgb(229 50 59 / .45)}
.live-badge i{width:.55em;height:.55em;border-radius:50%;background:#fff;animation:livepulse 1.2s ease-in-out infinite}
.hb-bar .live-badge{font-size:.66rem;padding:.22em .55em}
.hero__copy>.live-badge{margin-bottom:1rem;font-size:.8rem}
.detail__name .live-badge{display:flex;width:max-content;margin-bottom:.6rem}
@keyframes livepulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.25;transform:scale(.7)}}
.live-dot{display:inline-block;width:.6em;height:.6em;margin-right:.5em;border-radius:50%;vertical-align:.05em;
  background:var(--green);box-shadow:0 0 0 0 rgb(46 240 127 / .7);animation:livedot 1.4s ease-out infinite}
@keyframes livedot{0%{opacity:1;box-shadow:0 0 0 0 rgb(46 240 127 / .7)}50%{opacity:.35}
  70%{box-shadow:0 0 0 .55em rgb(46 240 127 / 0)}100%{opacity:1;box-shadow:0 0 0 0 rgb(46 240 127 / 0)}}
.hb-bar .live-dot{background:var(--on-green);animation-name:livedot-dark}
@keyframes livedot-dark{0%,100%{opacity:1}50%{opacity:.2}}
/* guias verticais decorativas cortavam o rosto na foto do topo */
.hero > .hb-lines{display:none}
@media (prefers-reduced-motion:reduce){.live-badge i,.live-dot{animation:none}}
</style>
</head>""", 1)

# ---------- foto do Pyero (seção "o mentor") — versões otimizadas em online/assets/pyero-palco-*.webp ----------
rx(r'<img src="assets/pyero\.[^"]*" srcset="[^"]*"',
   '<img src="assets/pyero-palco-880.webp" srcset="assets/pyero-palco-420.webp 420w, assets/pyero-palco-640.webp 640w, '
   'assets/pyero-palco-880.webp 880w, assets/pyero-palco-1200.webp 1200w"')
rx(r'(<img src="assets/pyero-palco-880\.webp"[^>]*?)width="1333" height="2000"', r'\1width="1493" height="2000"')

# ---------- logo "Nitro 10X 12.0 ONLINE" (topo e rodapé) ----------
rx(r'(<img src="assets/logo-nitro10x[^"]*"[^>]*class="hero__logo">)',
   r'<div class="logo-lockup logo-lockup--hero">\1<span class="logo-online">Online</span></div>')
rx(r'(<div class="ft__brand"[^>]*>)(<img src="assets/logo-nitro10x[^>]*>)',
   r'\1<div class="logo-lockup logo-lockup--ft">\2<span class="logo-online">Online</span></div>')
rep("</head>", """<style id="logo-online">
.logo-lockup{container-type:inline-size;display:flex;flex-direction:column;align-items:flex-end}
.logo-lockup img{width:100%!important;height:auto;margin:0!important;position:static!important;translate:none!important}
.logo-online{display:block;margin-top:-1.5cqi;padding:.9cqi 1.6cqi .9cqi 2.4cqi;border-radius:1cqi;
  font-family:var(--font-display);font-weight:800;font-stretch:125%;text-transform:uppercase;line-height:1;
  font-size:9.5cqi;letter-spacing:.38em;margin-right:-.38em;color:var(--on-green);background:var(--green);
  box-shadow:0 0 4cqi rgb(46 240 127 / .45)}
.logo-lockup--hero{filter:drop-shadow(0 18px 40px rgb(0 0 0 / .6))}
/* celular: ONLINE embaixo da logo, centralizado */
@media(max-width:999px){.logo-lockup--hero{width:min(210px,56%);margin:0 auto 1.4rem;align-items:center}
  .logo-lockup--hero .logo-online{margin-right:0}
  /* KV mais alto: corta o céu vazio acima das cabeças */
  .hero__media:not(#_){height:min(80vw,330px)}
  .hero__img:not(#_){object-position:50% 72%}
  /* o degradê escuro do topo pegava os rostos depois de subir o KV: fica só uma faixa fina */
  .hero__media:not(#_):after{background:linear-gradient(180deg,rgb(7 9 10 / .4) 0%,transparent 7%)}}
/* PC: ONLINE do lado da logo */
@media(min-width:1000px){.logo-lockup--hero{container-type:normal;flex-direction:row;align-items:center;gap:1.1rem;
    margin-block:clamp(1rem,2.4vw,1.4rem)}
  .logo-lockup--hero img{width:240px!important}
  .logo-lockup--hero .logo-online{margin:0;padding:.45rem .5rem .45rem .85rem;border-radius:4px;font-size:1.15rem;
    margin-right:0;box-shadow:0 0 22px rgb(46 240 127 / .45)}}
.logo-lockup--ft{width:140px}
.logo-lockup--ft .logo-online{box-shadow:none}
</style>
</head>""", 1)

# ---------- FAQ ----------
rep("Quem estará na sala?", "Para quem é o Nitro 10X Online?")
rep("Donos e sócios de empresa que faturam acima de R$1MM.",
    "Donos e sócios de empresa que querem crescer em 2027 com estratégia, sem perder a família e a fé.")
rep("Vou fechar negócios no evento?", "Como vou assistir?")
rep("Ninguém pode garantir. O Nitro cria o ambiente para conhecer pessoas e abrir conversas. O resultado depende da sua disposição em fazer acontecer.",
    "Ao vivo, pela internet. Depois da compra, você recebe por e-mail e WhatsApp o link de acesso. Basta um celular ou computador com boa conexão.")
rep("Qual ingresso devo escolher?", "Qual a diferença para o presencial?")
rep("Se quer viver os 3 dias, comece pelo Gold. Se as conexões são sua prioridade, compare o Platinum e o Diamond.",
    "O conteúdo do palco é o mesmo. O online não inclui assento na plenária, Welcome Kit e as experiências exclusivas do presencial, como área VIP e networking no local.")
rep("Posso levar meu sócio ou meu cônjuge?", "Posso assistir com meu sócio ou meu time?")
rep("Sim, e recomendamos. Cada participante precisa do próprio ingresso.",
    "Sim, e recomendamos assistir juntos. O acesso é individual: cada pessoa que for entrar com o próprio login precisa do seu ingresso.")
rep("O evento ao vivo não terá replay. O ingresso inclui a gravação do 10X Private e o material complementar digital.",
    "A transmissão ao vivo não terá replay. O ingresso inclui a gravação do 10X Private e o material complementar digital.")

# ---------- CTA final + rodapé ----------
rx(r'(<p class="hb-pill"[^>]*><i[^>]*></i>)03, 04 e 05 de dezembro · Alphaville \| Barueri - SP', r'\1 03, 04 e 05 de dezembro · <span class="live-badge"><i></i>Ao vivo</span> online')
rx(r'Garanta o\s+seu lugar na 12ª edição do Nitro 10X\.', 'Garanta o seu acesso <strong>ao vivo</strong> à 12ª edição do Nitro 10X.')
rx(r'<a href="https://www\.google\.com/maps/search/\?api=1&amp;query=Av\.\+Copacabana[^"]*"[^>]*>Alphaville - Barueri/SP</a>',
   "Online · ao vivo")
rep(">Data e local</h4>", ">Data e formato</h4>")

# ---------- checkout ----------
# o botão manda ingresso "Online ao vivo"; Gold é o fallback do código original
rx(r"const CHECKOUT = \{.*?\};", f"const CHECKOUT = {{\n    'Online ao vivo': '{CHECKOUT_ONLINE}',\n    Gold: '{CHECKOUT_ONLINE}'\n  }};")

# ---------- conferência ----------
for w in ["Alphaville", "Barueri", "Diamond", "Platinum", "presencial em", "seatmap\" id", "na sala"]:
    left = [m.start() for m in re.finditer(re.escape(w), s)]
    # ignora CSS (não aparece para o usuário)
    vis = [i for i in left if "{" not in s[max(0, i-60):i]]
    if vis:
        print(f"[aviso] ainda aparece '{w}' {len(vis)}x")

# ---------- sem selo vermelho "AO VIVO": fica só a bolinha verde ----------
s = s.replace('<span class="live-badge"><i></i>Ao vivo · 03 a 05 de dezembro · online</span>', '')  # acima do título
s = s.replace('<span class="live-badge"><i></i>Ao vivo</span> Ingresso Online', 'Ingresso Online')  # card do ingresso
s = s.replace('<span class="live-badge"><i></i>Ao vivo</span> online', '<span class="live-dot"></span>ao vivo · online')  # CTA final
s = s.replace('<span class="live-badge"><i></i>Ao vivo</span>', '<span><span class="live-dot"></span>Ao vivo</span>')  # barra do topo
assert 'class="live-badge"' not in s

# marca invisível: avisa quem abrir o HTML que ele é gerado (não editar à mão)
s = s.replace("<!DOCTYPE html>", "<!DOCTYPE html><!-- Gerado por build_online.py: edite o script, não este arquivo -->", 1)

out = ROOT / "online" / "index.html"
out.write_text(s, encoding="utf-8", newline="\n")  # mesmo resultado no Windows e no GitHub
print("ok ->", out)

