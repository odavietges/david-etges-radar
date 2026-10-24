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

O teste isolado de autenticação, pesquisa web e escrita passou (run 38155701493). A publicação editorial completa passou no [run 38157373354](https://github.com/odavietges/david-etges-radar/actions/runs/38157373354), com os quatro arquivos em um commit, Pages e validação pública. A reexecução [38158134968](https://github.com/odavietges/david-etges-radar/actions/runs/38158134968) passou sem duplicar a edição. O cron de publicação está habilitado em main. Após os testes, a antiga tarefa Publicar THE PULSE do ChatGPT foi pausada, sem exclusão; Avisar THE PULSE permanece ativa. Execuções diárias foram observadas. O sucesso de uma execução não garante pontualidade das próximas.

O token está exclusivamente no segredo Actions `CODEX_ACCESS_TOKEN`; não é uma chave de API faturada separadamente. A execução diária usará a autorização e os limites do workspace.

## Estrutura

- `index.html`: edição mais recente.
- `arquivo/index.html`: índice de edições.
- `arquivo/AAAA-MM-DD.html`: edição preservada por data.
- `arquivo/edicoes.json`: registro estruturado das edições.
- `arquivo/teste-nuvem.html`: teste histórico; não comprova sozinho a execução diária.

## Rotina diária

- 06:45 America/Cuiaba: início programado de pesquisa e publicação no workflow `Publicar THE PULSE com Codex`, cron `45 10 * * *` em UTC. A conclusão depende do tempo de pesquisa e deploy.
- 07:30 America/Cuiaba: `Monitorar pontualidade THE PULSE` consulta o head atual e exige edição corrente, Pages e validação pública. Falha identifica atraso real; não executa a validação obrigatória sobre um commit antigo. A tarefa hospedada Avisar THE PULSE permanece ativa diariamente às 07:30 AMT; seu prompt exige data corrente, deploy Pages e validação pública para o mesmo head antes do aviso de sucesso. Configuração conferida na interface oficial em 11/10/2026.

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

O workflow `Validar publicação pública` roda após confirmação do deploy, por dispatch explícito do publicador ou como conferência adicional de push. Usa somente leitura e não tem cron independente. Confere os quatro arquivos e todas as edições arquivadas contra a resposta pública do Pages. O aviso exige edição corrente, deploy concluído e essa conferência concluída com sucesso; um bloqueio da ferramenta web não deve ser confundido com falha do site. A prova deve corresponder ao head que contém a edição verificada.


## Correção de sequência — 23/10/2026

A execução agendada de validação 39981326166 conferiu corretamente 22/10 enquanto o publicador 39978629321 preparava 23/10. O commit 5ed1f1772bd9f7b5310df20821a47974fbc60fc0 teve deploy 39982109855 success e validação 39982211227 success, com comparação HTTPS dos quatro arquivos e de todo o histórico às 11:54 AMT. A publicação ocorreu atrasada; a causa específica do atraso do disparo ainda não foi demonstrada.

A confirmação obrigatória recebe SHA, data e identificador da execução publicadora; exige deploy success para o mesmo SHA antes da leitura pública. O cron 07:30 pertence apenas ao monitor de pontualidade. O aviso ChatGPT permanece separado e não anuncia edição antiga. O job publicador tem 40 minutos para comportar os limites internos de confirmação.

Testes sem escrita editorial ou credenciais: `python3 -m unittest discover -s tests -v`. O workflow `Testar segurança da publicação` executa esses testes em push e PR. Uma correção só é operacionalmente confirmada depois de testes hospedados, Pages e validação pública success no mesmo SHA. A próxima execução diária ainda deve comprovar o caminho de dispatch com identificação.
