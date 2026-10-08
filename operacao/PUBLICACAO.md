# Publicação diária do THE PULSE

## Operação em nuvem

As tarefas hospedadas no ChatGPT são Publicar THE PULSE (06:45) e Avisar THE PULSE (07:30), todos os dias no fuso America/Cuiaba (UTC-04:00). A integração GitHub conectada escreve no repositório público; GitHub Pages publica main. Não há executor local, token fornecido pelo usuário ou segredo neste repositório. O horário de início oferece 45 minutos; não é garantia de conclusão. O aviso informa pendência se a publicação não for confirmada.

## Transação de conteúdo

1. Calcular a data corrente no fuso indicado. Ler README, head de main, sua árvore, index.html e arquivo/edicoes.json.
2. Preservar todos os arquivos de datas anteriores byte a byte. Se a última edição ainda não tiver arquivo datado, preservá-la antes da substituição. Nunca fabricar uma edição para preencher um dia ausente.
3. Se a edição corrente já estiver completa e pública, validar e encerrar sem commit ou duplicata.
4. Pesquisar as fontes públicas, preparando HTML/CSS/JS autocontido com logo e identidade existentes. Manter regras editoriais: política neutra, alegações de conflitos atribuídas e cruzadas com fontes independentes, Pablo Spyer somente em conteúdo público verificável, monitoramento das entidades de turismo já aprovadas.
5. Preparar index.html, arquivo/YYYY-MM-DD.html, arquivo/edicoes.json e arquivo/index.html como um conjunto. Os registros ficam em ordem de data decrescente, sem duplicatas e com links existentes.
6. Identificar a edição com meta pulse-edition-date, meta pulse-edition-status=complete e body data-edition-date. No arquivo datado, informar que é uma edição arquivada. O link de histórico deve resolver corretamente a partir de ambas as localizações.
7. Validar dados, fontes, horários das cotações, estrutura HTML, JS, links e datas. Não preencher cotação indisponível com estimativa.
8. Pela integração GitHub, criar blobs (create_blob), árvore baseada na árvore lida (create_tree) e commit cujo parent é o head lido (create_commit). Atualizar main (update_ref) com expected_sha=head e force=false.
9. Em concorrência, reler o novo head e preservar as alterações. Não forçar a referência. Antes da atualização de main, nenhum blob ou commit isolado muda o site.
10. O workflow Validar publicação pública roda a cada push e compara os quatro arquivos e todas as edições do registro com as respectivas respostas HTTPS públicas, byte a byte. Aguarda até dez minutos a propagação do Pages. Só tem permissão de leitura e não modifica conteúdos. Uma execução success associada ao head que contém a edição é uma prova independente da publicação pública, consultável pela integração GitHub mesmo quando a ferramenta web não consegue abrir Pages. Exigir data da edição corrente no repositório, deploy Pages success e este workflow success. Resultado histórico de outra edição não basta.
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
