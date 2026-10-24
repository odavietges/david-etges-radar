# Publicação diária do THE PULSE

## Operação em nuvem

Migração autorizada e testada em 11/10/2026: GitHub Actions hospedado executa Codex CLI, autenticado com o segredo Actions CODEX_ACCESS_TOKEN do workspace Business. O token nunca entra no Git, no conteúdo ou nos logs; a execução usa os limites do workspace. Não depende do notebook. Não é um agendador recorrente nativo do Codex Cloud.

Publicar THE PULSE com Codex tem cron ativo `45 10 * * *` (06:45 America/Cuiaba). Esse é o início da pesquisa, não uma garantia de conclusão no minuto. O cron `30 11 * * *` (07:30) pertence ao workflow Monitorar pontualidade THE PULSE; a validação obrigatória não tem cron. Avisar THE PULSE permanece ativo no ChatGPT diariamente às 07:30 AMT: exige edição corrente, Pages success e validação pública success para o mesmo head antes de avisar. Sua configuração foi conferida na interface oficial.

Evidências: teste isolado [38155701493](https://github.com/odavietges/david-etges-radar/actions/runs/38155701493); publicação completa [38157373354](https://github.com/odavietges/david-etges-radar/actions/runs/38157373354), commit editorial 7f3a29f7d558beb2dcc24840e3ad53f6e4d411ac; correção da data visível e links b8e8c93bf0b177be5a87425f09d4c97baecf240e; reexecução idempotente [38158134968](https://github.com/odavietges/david-etges-radar/actions/runs/38158134968) concluída com sucesso sem novo commit editorial. A edição 006 de 11/10 está pública; as edições anteriores foram preservadas. As tentativas editoriais iniciais falharam antes do push; a arquitetura final usa pesquisa somente leitura e montagem determinística fora do agente.

O cron foi habilitado somente após esses testes. Execuções agendadas posteriores foram observadas; seus horários reais devem ser conferidos nos runs. GitHub Actions pode atrasar ou deixar de disparar eventos sob carga e pode desativar cron de repositório público após 60 dias sem atividade. Verificar runs em caso de falta de edição; não mudar sua data artificialmente. Renovar o segredo pelo fluxo oficial quando o token expirar.

## Transação de conteúdo

1. Calcular a data corrente no fuso indicado. Ler README, head de main, sua árvore, index.html e arquivo/edicoes.json.
2. Preservar todos os arquivos de datas anteriores byte a byte. Se a última edição ainda não tiver arquivo datado, preservá-la antes da substituição. Nunca fabricar uma edição para preencher um dia ausente.
3. Se a edição corrente já estiver completa e pública, validar e encerrar sem commit ou duplicata.
4. Pesquisar fontes públicas com Codex em modo somente leitura e obter dados estruturados, sem shell, arquivos ou credenciais Git. O renderizador confiável monta HTML a partir da edição existente, preservando CSS, JS e logo. Manter regras editoriais: política neutra, alegações de conflitos atribuídas e cruzadas com fontes independentes, Pablo Spyer somente em conteúdo público verificável, monitoramento das entidades de turismo já aprovadas.
5. Preparar index.html, arquivo/YYYY-MM-DD.html, arquivo/edicoes.json e arquivo/index.html como um conjunto. Os registros ficam em ordem de data decrescente, sem duplicatas e com links existentes.
6. Identificar a edição com meta pulse-edition-date, meta pulse-edition-status=complete e body data-edition-date. No arquivo datado, informar que é uma edição arquivada. O link de histórico deve resolver corretamente a partir de ambas as localizações.
7. Validar dados, fontes, horários das cotações, estrutura HTML, JS, links e datas. Não preencher cotação indisponível com estimativa.
8. Na rotina Actions, um job sem credenciais Git prepara e valida a edição. Apenas os quatro arquivos seguem em artefato para outro job, sem token Codex, que confere main, cria um único commit e faz push sem force. Fora dessa rotina, a integração continua sujeita aos controles oficiais; não contornar operações negadas.
9. Se main mudou durante a pesquisa, interromper sem sobrescrever alterações e revisar antes de nova execução. O push sem force também rejeita uma corrida posterior. Antes do push, a preparação não modifica o site.
10. O workflow Validar publicação pública é acionado pelo publicador após Pages built, com SHA/data/identificador explícitos, ou por push adicional. Em ambos os casos exige workflow Pages success do SHA antes de comparar os quatro arquivos e todas as edições do registro com as respectivas respostas HTTPS públicas, byte a byte. Aguarda até dez minutos a propagação do Pages. Só tem permissão de leitura e não modifica conteúdos. Uma execução success associada ao head que contém a edição é uma prova independente da publicação pública, consultável pela integração GitHub mesmo quando a ferramenta web não consegue abrir Pages. Exigir data da edição corrente no repositório, deploy Pages success e este workflow success. Resultado histórico de outra edição não basta.
11. Reler os quatro arquivos e confirmar seu conteúdo. Verificar o workflow Pages associado ao commit: completed e success. Abrir a URL pública e confirmar data, conteúdo, filtros, cards, arquivo datado e histórico.

## Aviso e falhas

Avisar THE PULSE só anuncia a edição corrente depois de confirmar os quatro arquivos, a página pública e o deploy. Usa o link fixo e até três destaques realmente presentes.

Em falha de pesquisa, escrita, aprovação, deploy ou leitura pública: preservar a última edição válida; informar data e etapa pendente; não enviar aviso de sucesso; não pausar ou excluir as tarefas por uma falha isolada. No máximo uma repetição para erro transitório. Negações de segurança não devem ser repetidas ou contornadas, e não autorizam credenciais alternativas. Commit confirmado com deploy pendente deve ser descrito dessa forma.

A página principal compara sua data com a data corrente em America/Cuiaba e sinaliza edição desatualizada. Arquivos datados continuam disponíveis para consulta histórica.

## Recuperação de 07/10/2026

O relato da execução de 06/10 no chat original atribui a falha ao mecanismo de segurança da escrita GitHub e registra a suspensão das duas tarefas. O motivo técnico específico da rejeição não estava disponível; não se atribui a falha a uma regra ou credencial não observada. Ambas as tarefas estavam pausadas na inspeção de 07/10.

A integração conectada aceitou a publicação atual: commit eb26545b8ddd9a53a5e97586b2c852fdef796bb0, deploy 37660322873 concluído com success, página pública verificada em 07/10. A edição 004 usa a data corrente e identifica a publicação extraordinária após o horário habitual. As edições 04 e 05 permanecem com seus blobs originais. 06/10 não foi publicada e não recebeu arquivo fictício.

As instruções das duas tarefas foram corrigidas para publicação conjunta, conferência pública e continuidade após falha. A geração inédita de uma próxima data pelo agendador precisa ser avaliada em sua execução efetiva; sucesso desta recuperação não garante permissões ou disponibilidade futuras da plataforma.

Site: https://odavietges.github.io/david-etges-radar/
Histórico: https://odavietges.github.io/david-etges-radar/arquivo/

## Diagnóstico de 08/10/2026 e limite de recuperação

A inspeção do repositório encontrou main em 5c26ea61962ad781adfc42c1e4775d6aa87629fc, sem commit nem arquivo datado de 08/10. Pages (37662465102) e Validar publicação pública (37662466170) concluíram com success para esse mesmo commit de 07/10. O registro contém 04, 05 e 07/10, sem duplicatas. A consulta de main informou protected=false e a lista de rulesets retornou vazia; esses resultados não revelam todas as políticas da integração.

O relato acessível da tarefa atribui a falha à revisão de segurança da escrita pela integração, antes do commit. O texto técnico da rejeição não está disponível nesse relato. A inspeção das permissões de GitHub mostrou Use my default, com padrão Allow low-risk actions. Essa configuração pode negar ações sensíveis, mas não prova por que esta chamada específica foi rejeitada. Não afirmar que a causa é token vencido, branch protection, conteúdo sensível ou ausência de permissão sem a resposta correspondente.

O workflow de conferência agora também executa às 11:30 UTC (07:30 America/Cuiaba). Em execução agendada, exige --require-current: após verificar os bytes públicos, falha se a edição não corresponde à data corrente. Em push, confere a publicação do commit sem converter uma edição histórica consistente em edição de hoje. O acionamento manual exige a data corrente por padrão. O resumo identifica GITHUB_SHA e data efetivamente verificada. Horários de GitHub Actions podem sofrer atraso; esse agendamento não garante entrega às 07:30.

Essa conferência é somente leitura, não gera notícias e não substitui Publicar THE PULSE nem Avisar THE PULSE. Um resultado success de push só confirma os bytes do commit: o aviso ainda deve exigir a data corrente e os dois workflows success para o SHA correto.

Não existe correção de YAML capaz de remover uma negativa externa de segurança. Não mover a escrita para outro conector, GitHub Actions, navegador ou credencial para evitar a negativa. Registrar a resposta exata quando disponível e encaminhar a revisão pelos controles oficiais da integração. Não repetir a operação negada, publicar conteúdo sem pesquisa atual, avançar a data nem pausar tarefas por falha isolada. As regras de transação atômica dos quatro arquivos permanecem obrigatórias.

A criação de objetos Git para a correção foi aceita nesta sessão pela conexão existente. Isso confirma apenas essas operações, não a remoção da regra externa nem a capacidade de uma futura tarefa agendada. A recuperação editorial de 08/10 usa nova pesquisa pública; nenhuma afirmação do relato anterior foi reutilizada como evidência de notícia.

## Caminho oficial hospedado

Codex access tokens: https://learn.chatgpt.com/docs/enterprise/access-tokens . GitHub schedule: https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule .

Commits feitos pelo GITHUB_TOKEN não acionam automaticamente builds Pages nem workflows de push. A rotina solicita POST /pages/builds com pages:write, exige status built para o SHA publicado, aciona Validar publicação pública via workflow_dispatch com actions:write e exige success para esse mesmo SHA e data corrente. Falha de permissão encerra a etapa; não usar outra credencial para contorná-la. Esse caminho passou no teste real e o cron foi habilitado depois da validação. Após confirmar a substituição testada e o cron em main, Publicar THE PULSE no ChatGPT foi pausada em 11/10/2026, sem exclusão. Avisar THE PULSE permanece ativa às 07:30.


## Sequência e monitoramento corrigidos em 23/10/2026

Esta seção substitui as descrições históricas anteriores sobre o cron do validador. A falha 39981326166 ocorreu antes do commit de 23/10; o deploy 39982109855 e a validação HTTPS 39982211227 confirmaram depois a edição desse dia. Isso comprova recuperação às 11:54, não cumprimento do prazo 07:30.

- `confirm()` mantém Pages built, verifica main antes/depois e dispara o validador com `expected_sha`, `expected_date` e `publication_id` (`GITHUB_RUN_ID-GITHUB_RUN_ATTEMPT`). Só aceita o run com esse identificador, SHA e success.
- O validador confere SHA do evento e checkout, exige deploy Pages success do SHA em até dez minutos e só então compara bytes públicos e todo o histórico. Divergência continua sendo erro; não há continue-on-error. Data corrente permanece obrigatória no dispatch diário.
- O monitor 07:30 consulta branches/main e o registro nesse SHA pela API, sem inferir atraso a partir do checkout antigo do cron. Exige edição corrente, deploy e validação success para o head. Ausência, pesquisa em andamento, erro ou provas pendentes no prazo são falha de pontualidade, com link do publicador quando disponível. Um atraso do próprio schedule limita a medição ao horário efetivo de execução; não comprova disponibilidade retroativa às 07:30.
- O monitor é somente leitura, não gera edições, não repete pesquisa e não altera o aviso ChatGPT. Mantém falhas reais visíveis, inclusive ausência completa da publicação. Se main mudar durante sua consulta, não anuncia sucesso.
- Limites: publicador 40 minutos, confirm() até 900 segundos para build e 1.000 para validação; validador 25 minutos, até 600 para deploy e 600 para bytes. Cada requisição pública respeita o saldo de prazo.
- Testar com `python3 -m unittest discover -s tests -v`; conferir teste hospedado, Pages e validação para o mesmo SHA de implantação e observar o dispatch identificado na próxima publicação diária. Reexecução editorial existente continua sem novo commit. Não executar nova pesquisa para testar infraestrutura.

Os quatro arquivos editoriais e todo o histórico permanecem fora desta correção operacional. Não mudar permissões de escrita, obter novas credenciais, usar force, enfraquecer isolamento da pesquisa ou retirar validações de identidade/fontes/histórico.
