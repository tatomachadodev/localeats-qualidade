# Atividade 1: Fundamentos e Características da Qualidade no LocalEats

## 1. Identificação

**Turma:** ADS5N26-2C 
**Data:** 22/09/2026

### Integrantes

| Nome | Usuário no GitHub |
|---|---|
| Tácio | @tatomachadodev |

**Elemento de Competência:** Compreender os fundamentos de qualidade de software e sua aplicação no desenvolvimento de sistemas.

**Aplicação:** <https://local-eats-unisenac.vercel.app/>

---

## 2. Tarefa 1: Fundamentos da qualidade

### 2.1 Necessidades explícitas e implícitas

| Tipo | Necessidade | Interessado | Consequência se não for atendida |
|---|---|---|---|
| Explícita | O sistema deve permitir que o usuário filtre os restaurantes por especialidade | Usuário final (Cliente) | O usuário terá dificuldade em encontrar o tipo de comida que deseja, podendo desistir de usar o aplicativo. |
| Explícita | O sistema deve permitir que o usuário consulte os seus pedidos realizados. | Usuário final (Cliente) | O usuário não saberá o status do seu pedido ou seu histórico, gerando ansiedade e contatos desnecessários com o suporte.|
| Implícita | O sistema deve carregar os resultados da pesquisa de restaurantes de forma rápida (em poucos segundos). | Usuário final (Cliente) | A demora no carregamento causará frustração, levando o usuário a abandonar o app antes de fazer o pedido. |
| Implícita | As senhas e os dados pessoais da conta do usuário devem ser armazenados com segurança. | Usuário final (Cliente) e Negócio | O vazamento de dados destruirá a confiança no aplicativo e poderá gerar problemas legais para os desenvolvedores/negócio. |

### 2.2 Questão sobre os fundamentos da qualidade

**Um sistema que implementa todas as funcionalidades explicitamente solicitadas pode, ainda assim, apresentar baixa qualidade? Justifiquem utilizando pelo menos uma necessidade implícita identificada pela equipe.**

Sim, pois a qualidade não se resume apenas a possuir as funcionalidades. Um sistema pode permitir a consulta de pedidos (explícita), mas se o aplicativo for excessivamente lento ou travar durante a busca, a experiência será ruim e o produto será considerado de baixa qualidade pelo usuário.

---

## 3. Tarefa 2: Exploração da aplicação


| Integrante | Funcionalidade | O que foi realizado | O que foi observado | Evidência |
|---|---|---|---|---|
| Tácio | Fazer pedidos | Seleção de um restaurante e adição de pratos no carrinho e finalizar pedido. Tentativa de acessar o carrinho sem nenhum item. | Ao clicar em finalizar pedido, o pedido foi finalizado com sucesso. Na tentativa de acessar o carrinho sem itens não foi possível encontrar. | [ver evidência](evidencias/tacio-fazer-pedido.png) |

---

## 4. Tarefa 3: Requisitos e características de qualidade


| Integrante | Requisito de Qualidade | Característica ou subcaracterística | Justificativa | Como avaliar |
|---|---|---|---|---|
| Tácio | O sistema deve permitir que o usuário cancele um pedido recém-realizado em até 2 cliques a partir da tela de acompanhamento, confirmando o cancelamento. | Usabilidade, Facilidade de operação | No LocalEats, se o cliente fizer um pedido por engano, um fluxo de cancelamento simples e ágil evita cobranças indevidas ao usuário e impede que o restaurante comece a preparar um prato que será descartado | Medir a quantidade de cliques necessários para concluir o cancelamento a partir da tela do pedido e cronometrar o tempo que o sistema leva para atualizar o status para "Cancelado". |

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**  
Google Gemini

**Como foi utilizada:**  
Foi utilizada para auxiliar na correção e no refinamento da escrita das respostas

**Como as respostas foram verificadas:**  
Foi feita a leitura do conteúdo gerado para confirmar se as repostas mantiveram a mesma ideia.
