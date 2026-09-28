# Atividade 3: Estratégia e Projeto de Testes do LocalEats

## 1. Identificação

**Turma:** ADS5N26-2C 
**Data:** 22/09/2026

### Integrantes

| Nome | Usuário no GitHub |
|---|---|
| Tácio | @tatomachadodev |

**Elemento de Competência:** Planejar e projetar testes selecionando técnicas adequadas.

**Aplicação:** <https://local-eats-unisenac.vercel.app/>

---

## 2. Tarefa 1: Planejamento dos testes

### 2.1 Objetivo dos testes

Verificar se o processo de seleção de pratos, montagem do carrinho e finalização da compra no LocalEats funcionam corretamente, garantindo que pedidos válidos sejam concluídos e que tentativas inválidas sejam devidamente bloqueadas pelo sistema.

### 2.2 Escopo

#### Funcionalidades incluídas

| Integrante | Funcionalidade incluída | O que será verificado |
|---|---|---|
| Tácio | Fazer Pedido | O fluxo de seleção de pratos, adição/remoção do carrinho e a confirmação do pedido final |

#### Funcionalidade não incluída

| Funcionalidade não incluída | Justificativa |
|---|---|
| Criar conta e autenticação | Não fazem parte do fluxo principal de montagem e finalização do carrinho focado neste ciclo de testes |

### 2.3 Abordagem

| Item | Decisão da equipe | Justificativa |
|---|---|---|
| Níveis de teste | Teste de Sistema | O fluxo de realização do pedido será validado do início ao fim diretamente através da interface do usuário |
| Tipos de teste | Funcional | O objetivo é validar o cumprimento das regras de negócio do processo de compra |
| Perspectiva caixa-preta ou caixa-branca | Caixa-preta | As validações serão focadas nas entradas fornecidas na tela e nas respostas visíveis, sem análise de código-fonte |
| Técnicas de teste | Tabela de Decisão | A finalização do pedido depende da combinação de várias condições |

### 2.4 Ambiente e responsabilidades

| Item | Definição |
|---|---|
| Ambiente necessário | Navegador web atualizado (Chrome/Firefox), acesso à URL `https://local-eats-unisenac.vercel.app/` e conexão estável à internet. |
| Responsáveis pelo planejamento | Tácio |
| Responsáveis pela especificação dos casos | Tácio |
| Responsáveis pela futura execução | Tácio |

### 2.5 Critérios

| Critério | Definição da equipe |
|---|---|
| Entrada | Aplicação LocalEats acessível online com catálogo de restaurantes e pratos carregados normalmente |
| Saída | 100% dos casos de teste planejados documentados e validados na matriz de rastreabilidade |
| Suspensão | Indisponibilidade da aplicação web ou falha geral ao tentar carregar o cardápio dos restaurantes |

---

## 3. Tarefa 2: Riscos e técnicas de teste

### 3.1 Análise dos riscos

| ID | Integrante | Funcionalidade | Risco | Consequência | Probabilidade | Impacto | Prioridade | Justificativa |
|---|---|---|---|---|:---:|:---:|:---:|---|
| R01 | Tácio | Fazer Pedido | Permitir a finalização do pedido com o carrinho vazio | Envio de pedidos nulos para o restaurante, gerando falhas no sistema e frustração ao cliente. | Média | Alto | Alta | Compromete diretamente o fluxo principal de vendas e o funcionamento do serviço do restaurante |
| R02 | Tácio | Fazer Pedido | Permitir finalizar o pedido sem que o usuário esteja autenticado | Impossibilidade de associar o pedido a uma conta e de consultar o histórico de pedidos | Média | Alto | Alta | O LocalEats necessita do usuário autenticado para vincular e gerir os pedidos |

### 3.2 Aplicação das técnicas

#### Análise do integrante 1

**Integrante:** Tácio  
**Funcionalidade:** Fazer Pedido  
**Risco relacionado:** R01 e R02  
**Técnica escolhida:** Tabela de Decisão

**Por que a técnica foi escolhida:**  
A Tabela de Decisão é adequada pois a conclusão do pedido depende do cumprimento simultâneo das regras de ter itens no carrinho e de o usuário estar com a sessão ativa.

**Aplicação da técnica:**  

| Condições/Regras | Regra 1 | Regra 2 | Regra 3 |
|---|---|---|---|
| O carrinho possui itens selecionados? | Sim | Sim | Não |
| O usuário está autenticado (logado)? | Sim | Não | Sim |
| **Resultado esperado** | Permitir finalizar o pedido com sucesso | Bloquear finalização e solicitar autenticação | Bloquear e exibir aviso de carrinho vazio | 

**Casos derivados:**
- CT01: Concluir pedido com sucesso estando autenticado e com itens (Regra 1)
- CT02: Impedir acesso ao fluxo de pedidos sem autenticação do usuário (Regra 2)
- CT03: Impedir finalização do pedido com carrinho vazio (Regra 3)

---

## 4. Tarefa 3: Casos de teste e rastreabilidade

### 4.1 Casos de teste

### CT01: Concluir pedido com sucesso estando autenticado e com itens no carrinho

**Integrante responsável:** Tácio  
**Funcionalidade:** Fazer Pedido  
**Risco ou requisito relacionado:** R01 e R02  
**Técnica utilizada:** Tabela de Decisão (Regra 1)

**Pré-condição:**  
O usuário está autenticado na plataforma e existem restaurantes com cardápio disponível.

**Dados de entrada:**  
Restaurante selecionado, 1 item adicionado ao carrinho

**Passos:**
1. Acessar o sistema com o perfil autenticado.
2. Navegar até a lista de restaurantes e selecionar um estabelecimento.
3. Adicionar um item ao carrinho.
4. Clicar em Finalizar Pedido.

**Resultado esperado:**  
O pedido é finalizado com sucesso, exibindo mensagem de confirmação e registrando o pedido no histórico.

---

### CT02: Impedir acesso ao fluxo de pedidos sem autenticação do usuário

**Integrante responsável:** Tácio  
**Funcionalidade:** Fazer Pedido  
**Risco ou requisito relacionado:** R02  
**Técnica utilizada:** Tabela de Decisão (Regra 2)

**Pré-condição:**  
O usuário está na plataforma em modo visitante (não logado).

**Dados de entrada:**  
NENHUM

**Passos:**
1. Acessar o LocalEats sem realizar autenticação.
2. Tentar acessar a lista de restaurantes ou o fluxo de pedidos.

**Resultado esperado:**  
O sistema bloqueia o acesso e exige/redireciona o usuário diretamente para a tela de login.

---

### CT03: Impedir finalização do pedido com carrinho vazio

**Integrante responsável:** Tácio  
**Funcionalidade:** Fazer Pedido  
**Risco ou requisito relacionado:** R01  
**Técnica utilizada:** Tabela de Decisão (Regra 3)

**Pré-condição:**  
O usuário realiza o login no sistema com sucesso.

**Dados de entrada:**  
NENHUM (carrinho sem itens)

**Passos:**
1. Acessar o sistema com perfil autenticado.
2. Acessar o carrinho de compras sem adicionar nenhum prato.
3. Tentar acionar o botão de finalização do pedido.

**Resultado esperado:**  
O botão de finalização permanece desabilitado ou o sistema exibe uma mensagem informando que é necessário adicionar itens para prosseguir.

---

### 4.2 Matriz de rastreabilidade

| Integrante | Funcionalidade | Risco ou requisito | Técnica utilizada | Casos de teste |
|---|---|---|---|---|
| Tácio | Fazer Pedido | R01 (Carrinho vazio) e R02 (Sem autenticação) | Tabela de Decisão | CT01, CT02 e CT03 |

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**  
Google Gemini

**Como foi utilizada:**  
A ferramenta foi utilizada para auxiliar na estruturação do plano de testes, definição de riscos, construção da tabela de decisão e elaboração dos casos de teste.

**Uma sugestão que precisou ser alterada ou rejeitada:**  
A IA sugeriu inicialmente validar campos de endereço de entrega e testar o bloqueio de usuário não logado apenas na etapa final do carrinho no CT02. A sugestão foi alterada porque o sistema não possui campo de endereço e bloqueia a navegação para os restaurantes logo no início se não houver login.

**Como as respostas foram verificadas:**  
Foi realizada a verificação prática diretamente na interface da aplicação LocalEats para garantir que as pré-condições, passos e resultados esperados estivessem alinhados com o comportamento real do sistema.