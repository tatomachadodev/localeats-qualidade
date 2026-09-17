# Atividade 2: Organização da Qualidade no LocalEats

## 1. Identificação

**Turma:** ADS5N26-2C 
**Data:** 22/09/2026

### Integrantes

| Nome | Usuário no GitHub |
|---|---|
| Tácio | @tatomachadodev |

**Elemento de Competência:** Identificar papéis, responsabilidades e competências relacionadas às atividades de qualidade e testes.

---

## 2. Tarefa 1: Diagnóstico da situação

### 2.1 Problemas organizacionais

| Problema identificado | Possível consequência para o produto ou para a equipe |
|---|---|
| Ausência de critérios claros de aceitação e de "funcionalidade pronta" | Entrega de funcionalidades incompletas ou com falhas para os usuários, gerando insatisfação dos clientes e retrabalho constante para a equipe para corrigir bugs em produção |
| Crença de que a qualidade e os testes são responsabilidade exclusiva do QA | Sobrecarga do profissional de QA, criação de gargalos na esteira de desenvolvimento e descomprometimento dos desenvolvedores com a qualidade do próprio código. |
| Falta de registro e acompanhamento dos defeitos encontrados | Perda de rastreabilidade de falhas conhecidas, fazendo com que bugs antigos continuem afetando o sistema sem priorização para correção. |

### 2.2 Responsabilidade pela qualidade

**A qualidade do LocalEats deve ser responsabilidade exclusiva do profissional de QA? Justifiquem.**

Não, a qualidade deve ser uma responsabilidade compartilhada por toda a equipe. O QA atua na estratégia, prevenção de falhas e disseminação de boas práticas, mas os desenvolvedores devem garantir a qualidade do código com testes unitários e o Product Owner deve garantir requisitos claros. Isolar a qualidade no QA gera gargalos e reduz a responsabilidade do time sobre o produto.

---

## 3. Tarefa 2: Papéis e competências

| Integrante | Papel analisado | Responsabilidades relacionadas à qualidade | Competências técnicas | Competências comportamentais |
|---|---|---|---|---|
| Tácio | Responsável pelo Produto | Definir critérios de aceitação claros para as funcionalidades, validar se as entregas atendem às necessidades do negócio/usuário e priorizar a correção de defeitos junto ao backlog.| Engenharia de Requisitos, Metodologias Ágeis (Scrum/Kanban) e escrita de Histórias de Usuário (User Stories). | Visão de negócio, comunicação clara, capacidade de decisão e facilidade em negociação |
| Tácio | Desenvolvedor(a) | Escrever código limpo e testável, criar e executar testes unitários, realizar revisão de código (code review) e corrigir os defeitos identificados. | Linguagens de programação do projeto, frameworks de testes unitários (ex: Jest/JUnit), versionamento de código (Git) e padrões de projeto. | Atenção a detalhes, trabalho colaborativo em equipe, abertura a feedbacks e resolução de problemas. |
| Tácio | Analista de Qualidade (QA) | Planejar a estratégia de testes do sistema, automatizar testes funcionais e de regressão, auxiliar o time na identificação de cenários de erro e registrar/acompanhar defeitos. | Ferramentas de automação de testes (ex: Cypress, Playwright), testes de API, gestão de defeitos e estratégias de modelagem de teste. | Pensamento crítico, perfil investigativo, boa comunicação e empatia para disseminar a cultura de qualidade no time |
| Tácio | Liderança Técnica (Tech Lead)| Definir padrões de arquitetura e qualidade de código, conduzir revisões técnicas complexas, garantir boas práticas de integração e aprovar o lançamento de novas versões. | Arquitetura de Software, práticas de CI/CD, segurança de código e análise avançada de desempenho. | Liderança, mentoria, visão holística do sistema e gestão de conflitos técnicos. |

---

## 4. Tarefa 3: Matriz de responsabilidades

Utilizem:

- **R:** responsável por executar a atividade;
- **A:** aprovador ou responsável final;
- **C:** consultado antes da execução ou decisão;
- **I:** informado sobre o resultado.

| Atividade de qualidade | Product Owner | Desenvolvedor | Analista de Qualidade | Liderança Técnica |
|---|:---:|:---:|:---:|:---:|
| Definir critérios de aceitação | R/A | C | C | I |
| Revisar requisitos | A | R | R | C |
| Implementar a funcionalidade | I | R/A | I | C |
| Revisar o código | I | R | C | A |
| Criar testes unitários | I | R/A | C | C |
| Planejar e executar testes do sistema | I | C | R/A | C |
| Registrar e acompanhar defeitos | A | C | R | I |
| Priorizar a correção dos defeitos | R/A | C | C | C |
| Aprovar a disponibilização da versão | C | I | C | R/A |

### 4.1 Lacuna ou conflito encontrado

**Lacuna ou conflito:**  
Aprovar a disponibilização da versão.

**Consequência:**  
Sem a matriz, a responsabilidade ficava sem dono claro ou gerava atrito entre negócios e tecnologia. Se apenas o Product Owner aprovar sem consultar a área técnica, um sistema instável pode ir para produção. Ao definir o Tech Lead como o aprovador final (A) munido dos relatos do QA e do PO, elimina-se a dúvida sobre quem autoriza o deploy.

### 4.2 Práticas de QA recomendadas

| Prática recomendada | Problema que ajuda a resolver | Papéis envolvidos |
|---|---|---|
| Definição de Pronto | Falta de clareza sobre quando uma funcionalidade está realmente finalizada e envio de código sem testes para produção | Product Owner, Desenvolvedor, QA e Tech Lead |
| Sessões de Three Amigos | Requisitos mal compreendidos, ausência de critérios de aceitação e testes criados de forma isolada apenas no fim do ciclo. | Product Owner, Desenvolvedor e QA |

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**  
Google Gemini

**Como foi utilizada:**  
Foi utilizada para auxiliar na correção e no refinamento da escrita das respostas, também para pesquisar alguns tempos específicos.

**Como as respostas foram verificadas:**  
Foi feita a leitura do conteúdo gerado para confirmar se as repostas mantiveram a mesma ideia.