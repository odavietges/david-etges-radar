# THE PULSE · por David Etges

**O que move o mundo. O que muda sua decisão.**

Curadoria executiva diária de economia, mercados, política, geopolítica, conflitos, tecnologia, IA, turismo, hotelaria, parques, real estate turístico, capital global, offshore e cripto.

Site público: https://odavietges.github.io/david-etges-radar/

Histórico: https://odavietges.github.io/david-etges-radar/arquivo/

## Arquitetura cloud-only

A operação diária não depende do notebook do usuário.

Fluxo:

ChatGPT Automation → GitHub Connector → repositório → GitHub Pages → navegador.

## Estrutura

- `index.html`: edição mais recente.
- `arquivo/index.html`: índice de edições.
- `arquivo/AAAA-MM-DD.html`: edição preservada por data.
- `arquivo/edicoes.json`: registro estruturado das edições.
- `arquivo/teste-nuvem.html`: prova do fluxo ChatGPT → GitHub → GitHub Pages.

## Rotina diária

- 07:15 America/Cuiaba: a automação pesquisa, gera e publica a edição.
- 07:30 America/Cuiaba: a automação de aviso confirma se a edição do dia está publicada e envia o link fixo.

## Regras de publicação

1. Ler o `index.html` vigente.
2. Preservar a edição anterior em `arquivo/AAAA-MM-DD.html`.
3. Criar ou atualizar a edição do dia.
4. Atualizar `index.html`.
5. Atualizar `arquivo/edicoes.json`.
6. Atualizar `arquivo/index.html`.
7. Reler os arquivos pela integração GitHub para confirmar a escrita.
8. Nunca apagar histórico.
9. Se pesquisa ou escrita falhar, manter a última edição válida no ar.
10. Não publicar edição vazia nem inventar conteúdo.

## Conteúdo permanente

### Política & Geopolítica
Brasil e mundo, com atenção especial aos EUA, sempre de forma factual e neutra.

### Conflitos & Segurança Global
Rússia–Ucrânia; Israel, Irã e Oriente Médio; EUA–Irã; Hormuz; Yemen/Houthis/Mar Vermelho/Bab el-Mandeb; China–Taiwan; Coreias; Índia–Paquistão; e outros conflitos relevantes quando houver fato novo material.

### Análise de Mercado · Pablo Spyer
Usar somente conteúdo público recente e verificável, identificado explicitamente como visão de Pablo Spyer. Se não houver atualização relevante, declarar isso.

### Turismo & Hotelaria
Priorizar PANROTAS, Hotelier News, SINDEPAT, ADIBRA, ADIT Brasil, IAAPA, Secovi-SP e Turismo Compartilhado, com foco em resorts, parques, atrações, multipropriedade, timeshare, condo-hotel, branded residences, real estate turístico, investimentos, expansão e demanda.

## Identidade visual

- Fundo: `#000000`
- Texto: `#FFFFFF`
- Dourado oficial: `#D4A15E`
- Mobile-first
- Sem gradientes, glow ou efeitos supérfluos
- Logo preservada sem alteração geométrica

## Segurança

Nenhum token, senha, cookie, API key ou credencial deve ser salvo no repositório.

## Versionamento

Commit recomendado:

```
THE PULSE — YYYY-MM-DD
```

Reexecuções no mesmo dia devem atualizar a mesma edição, sem duplicatas.
