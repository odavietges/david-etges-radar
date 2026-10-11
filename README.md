# THE PULSE · por David Etges

**O que move o mundo. O que muda sua decisão.**

Curadoria executiva diária de economia, mercados, política, geopolítica, conflitos, tecnologia, IA, turismo, hotelaria, parques, real estate turístico, capital global, offshore e cripto.

Site público: https://odavietges.github.io/david-etges-radar/

Histórico: https://odavietges.github.io/david-etges-radar/arquivo/

## Arquitetura cloud-only

A operação diária não depende do notebook do usuário.

Fluxo:

Caminho hospedado implantado e testado em 11/10/2026:

GitHub Actions hospedado → pesquisa Codex CLI com token Business → montagem pelo renderizador confiável → validação dos quatro arquivos → commit único → solicitação explícita de build Pages → validação pública.

O teste isolado de autenticação, pesquisa web e escrita passou (run 38155701493). A publicação editorial completa passou no [run 38157373354](https://github.com/odavietges/david-etges-radar/actions/runs/38157373354), com os quatro arquivos em um commit, Pages e validação pública. A reexecução [38158134968](https://github.com/odavietges/david-etges-radar/actions/runs/38158134968) passou sem duplicar a edição. O cron de publicação está habilitado em main. Após os testes, a antiga tarefa Publicar THE PULSE do ChatGPT foi pausada, sem exclusão; Avisar THE PULSE permanece ativa. A primeira execução diária após a ativação ainda deve ser observada; testes manuais não comprovam disparos futuros.

O token está exclusivamente no segredo Actions `CODEX_ACCESS_TOKEN`; não é uma chave de API faturada separadamente. A execução diária usará a autorização e os limites do workspace.

## Estrutura

- `index.html`: edição mais recente.
- `arquivo/index.html`: índice de edições.
- `arquivo/AAAA-MM-DD.html`: edição preservada por data.
- `arquivo/edicoes.json`: registro estruturado das edições.
- `arquivo/teste-nuvem.html`: teste histórico; não comprova sozinho a execução diária.

## Rotina diária

- 06:45 America/Cuiaba: início programado de pesquisa e publicação no workflow `Publicar THE PULSE com Codex`, cron `45 10 * * *` em UTC. A conclusão depende do tempo de pesquisa e deploy.
- 07:30 America/Cuiaba: o workflow existente confere a data e os bytes públicos. A tarefa hospedada Avisar THE PULSE permanece ativa diariamente às 07:30 AMT; seu prompt exige data corrente, deploy Pages e validação pública para o mesmo head antes do aviso de sucesso. Configuração conferida na interface oficial em 11/10/2026.

## Regras de publicação

1. Ler head, árvore, edição vigente e registro completo.
2. Preservar os bytes de todos os arquivos de edições anteriores.
3. Preparar e validar os quatro arquivos da edição antes de atualizar main.
4. Criar um único commit dos quatro arquivos, baseado no head vigente.
5. Conferir o head remoto e atualizar main por push sem force; jamais forçar ou apagar histórico.
6. Reler os quatro arquivos, exigir deploy Pages concluído com success e conferir a página pública.
7. Só anunciar sucesso quando a data pública for a data corrente em America/Cuiaba.
8. Em falha, preservar a última edição válida, explicitar a etapa pendente e manter as tarefas agendadas.
9. Não inventar conteúdo, cotações, opiniões, datas ou edições ausentes.
10. Seguir [operacao/PUBLICACAO.md](operacao/PUBLICACAO.md).

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

Reexecuções no mesmo dia validam a edição já completa, sem duplicatas. Correções editoriais posteriores exigem motivo explícito e preservação do histórico Git.

## Conferência pública automática

O workflow `Validar publicação pública` roda em GitHub Actions a cada push, usando somente leitura. Confere os quatro arquivos e todas as edições arquivadas contra a resposta pública do Pages. O aviso exige edição corrente, deploy concluído e essa conferência concluída com sucesso; um bloqueio da ferramenta web não deve ser confundido com falha do site. A prova deve corresponder ao head que contém a edição verificada.
