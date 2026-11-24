// Worker "nitro-online-lp" — serve a LP em https://lp.nitro10x.com.br/nitro-online/
// Rota no Cloudflare: lp.nitro10x.com.br/nitro-online*  (zona nitro10x.com.br)
// Busca a página publicada no GitHub Pages; qualquer outro caminho segue para o site atual sem alteração.
const ORIGEM = "https://joaoelias98.github.io/nitro-online-lp/online";
const BASE = "/nitro-online";

export default {
  async fetch(request) {
    const url = new URL(request.url);

    // Segurança: só mexe em /nitro-online e /nitro-online/...; o resto vai para o site atual
    if (url.pathname !== BASE && !url.pathname.startsWith(BASE + "/")) {
      return fetch(request);
    }

    // /nitro-online -> /nitro-online/ (os caminhos das imagens são relativos)
    if (url.pathname === BASE) {
      return Response.redirect(url.origin + BASE + "/" + url.search, 301);
    }

    if (request.method !== "GET" && request.method !== "HEAD") {
      return new Response("Método não permitido", { status: 405 });
    }

    const resto = url.pathname.slice(BASE.length); // "/", "/assets/x.webp", ...
    const resp = await fetch(ORIGEM + resto, {
      method: request.method,
      cf: { cacheEverything: true, cacheTtl: 60 },
    });

    const headers = new Headers(resp.headers);
    for (const h of ["x-github-request-id", "x-fastly-request-id", "x-served-by", "x-cache", "x-cache-hits", "x-timer", "via", "x-proxy-cache"]) {
      headers.delete(h);
    }
    // HTML sempre fresco (mudanças aparecem em ~1 min); imagens podem ficar em cache por mais tempo
    const tipo = headers.get("content-type") || "";
    headers.set("cache-control", tipo.includes("text/html") ? "public, max-age=60" : "public, max-age=86400");

    return new Response(resp.body, { status: resp.status, headers });
  },
};
