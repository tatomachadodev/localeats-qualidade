# Atividade 4: Testes Automatizados do LocalEats

---

## 1. Identificação

- **Turma:** ADS5N26-2C
- **Modalidade:** Individual
- **Repositório:** [Repositório Github](https://github.com/tatomachadodev/localeats-qualidade)
- **Diretório da atividade:** [link direto para o diretório](https://github.com/tatomachadodev/localeats-qualidade/tree/main/Atividades/atividade-04)
- **Data da última execução:** 03/11/2026

### Integrantes

1. Tácio Würdig

---

## 2. Integrantes e responsabilidades

Preencha uma linha para cada teste. Os testes unitários devem usar identificadores `TU01`, `TU02` e seguintes. Os testes funcionais devem usar `TF01`, `TF02` e seguintes.


| ID | Integrante responsável | Tipo | Comportamento verificado | Arquivo e função de teste |
|---|---|---|---|---|
| TU01 | Tácio Wurdig | Unitário | Pedido de R$ 150,00 recebe R$ 15,00 de desconto | `tests/test_regras_localeats.py::test_pedido_de_150_recebe_desconto_de_15` |
| TU02 | Tácio Wurdig | Unitário | Pedido abaixo de R$ 100,00 não recebe desconto | `tests/test_regras_localeats.py::test_pedido_abaixo_de_100_nao_recebe_desconto` |
| TU03 | Tácio Wurdig | Unitário | Limite exato de R$ 100,00 recebe desconto de R$ 10,00 | `tests/test_regras_localeats.py::test_pedido_de_100_recebe_desconto_de_10` |
| TU04 | Tácio Wurdig | Unitário | Valor negativo gera `ValueError` | `tests/test_regras_localeats.py::test_valor_negativo_gera_value_error` |
| TF01 | Tácio Wurdig | Funcional | Selecionar a categoria Italiana e verificar que só restaurantes dessa categoria são listados | `tests/test_localeats.py::test_selecionar_categoria_italiana_exibe_restaurantes_da_categoria` |


### Quantidades mínimas

- **Individual:** uma função, dois testes unitários e um teste funcional.

O teste funcional possui pelo menos duas assertions.

---

## 3. Testes unitários

Cada integrante deve escolher uma regra diferente, implementar a função correspondente e criar pelo menos dois testes unitários.

### Regras disponíveis

#### Regra 1: valor mínimo do pedido

```python
pedido_atingiu_valor_minimo(valor_pedido)
```

- Retorna `True` para pedidos de R$ 30,00 ou mais.
- Retorna `False` para pedidos abaixo de R$ 30,00.
- Gera `ValueError` para valores negativos.

#### Regra 2: desconto do pedido

```python
calcular_desconto(valor_pedido)
```

- Retorna `0` para pedidos abaixo de R$ 100,00.
- Retorna 10% do valor para pedidos de R$ 100,00 ou mais.
- Retorna apenas o valor do desconto.
- Gera `ValueError` para valores negativos.

#### Regra 3: quantidade de itens

```python
quantidade_itens_valida(quantidade)
```

- Retorna `True` para quantidades entre 1 e 10.
- Retorna `False` para zero ou quantidades acima de 10.
- Gera `ValueError` para quantidades negativas.

#### Regra 4: avaliação do restaurante

```python
avaliacao_valida(nota)
```

- Retorna `True` para notas entre 1 e 5.
- Retorna `False` para notas abaixo de 1 ou acima de 5.

### Registro das regras implementadas

#### Regra de Tácio Würdig

- **Regra escolhida:** Regra 2, desconto do pedido
- **Função implementada:** `calcular_desconto`
- **Arquivo da implementação:** `src/regras_localeats.py`
- **Testes criados:** `test_pedido_de_150_recebe_desconto_de_15`; `test_pedido_abaixo_de_100_nao_recebe_desconto`; `test_pedido_de_100_recebe_desconto_de_10`; `test_valor_negativo_gera_value_error`.
- **Comportamentos verificados:** pedido de R$ 150,00 recebe R$ 15,00 de desconto; pedido abaixo de R$ 100,00 não recebe desconto; o limite exato de R$ 100,00 recebe R$ 10,00; valor negativo gera `ValueError`.

---

## 4. Aplicação do TDD

Cada integrante deve registrar de forma breve o desenvolvimento orientado a testes da própria regra.

### TDD de Tácio Würdig

- **Regra escolhida:** Regra 2, desconto do pedido (`calcular_desconto`)
- **Primeiro teste escrito:** `test_pedido_de_150_recebe_desconto_de_15`
- **Por que o teste falhou inicialmente:** a função existia, mas ainda não retornava nada. O pytest mostrou `assert None == 15`.
- **Implementação mínima realizada:** fiz a função retornar `valor_pedido * 0.10`, o suficiente para o teste de R$ 150,00 passar.
- **Segundo teste escrito:** `test_pedido_abaixo_de_100_nao_recebe_desconto`
- **Melhoria ou refatoração realizada:** adicionei o `if valor_pedido >= 100`, retornando 0 nos demais casos. Depois escrevi o teste do limite de R$ 100,00 (que já passava) e o teste do valor negativo, e incluí na função a validação que lança `ValueError`.


---

## 5. Testes funcionais com Playwright

Cada integrante deve automatizar um fluxo diferente pela interface do LocalEats.

**Sistema:** https://local-eats-unisenac.vercel.app/

### Fluxos possíveis

- verificar a apresentação da página inicial;
- pesquisar um restaurante;
- selecionar uma categoria;
- verificar restaurantes de uma categoria;
- verificar informações apresentadas em um restaurante;
- criar uma conta ou entrar no sistema, se o fluxo estiver disponível;
- favoritar ou desfavoritar um restaurante;
- consultar pedidos;
- automatizar outro comportamento estável identificado durante a exploração.

### Requisitos de cada teste funcional

- acessar o LocalEats;
- realizar pelo menos uma interação pela interface;
- utilizar locators do Playwright;
- possuir pelo menos duas assertions;
- verificar resultados observáveis;
- não utilizar `time.sleep`;
- executar com pytest;
- identificar o integrante responsável no código.

### Teste funcional de Tácio Würdig

- **ID:** `TF01`
- **Fluxo automatizado:** seleção da categoria Italiana na página inicial do LocalEats, após login
- **Interação realizada:** entrei no sistema com uma conta de teste e cliquei no botão "Italiana"
- **Primeira assertion:** a lista passa a exibir 3 restaurantes da categoria Italiana
- **Segunda assertion:** nenhum restaurante da categoria Japonesa continua na lista
- **Arquivo e função:** `tests/test_localeats.py::test_selecionar_categoria_italiana_exibe_restaurantes_da_categoria`
- **Resultado final:** aprovado

---

## 6. Resultado da execução

Execute todos os testes no PowerShell:

```powershell
python -m pytest -v | Tee-Object -FilePath relatorio-pytest.txt
```

Depois, registre o resultado:

- **Quantidade total de testes:** 5
- **Testes aprovados:** 5
- **Testes reprovados:** 0
- **Link para o relatório:** [relatorio-pytest.txt](relatorio-pytest.txt)
- **Observações:** Todos os testes foram aprovados

---

## 7. Explicações individuais

Cada integrante deve escolher um teste de sua responsabilidade e demonstrar compreensão sobre o código entregue.

### Explicação do teste de Tácio Würdig

- **Teste escolhido:** `test_pedido_de_100_recebe_desconto_de_10`
- **Comportamento verificado:** o limite exato da regra de desconto. A regra diz que pedidos de R$ 100,00 ou mais recebem 10% de desconto, então um pedido de exatamente R$ 100,00 já deve receber desconto.
- **Dados ou estado inicial:** o valor do pedido é 100, passado direto para a função `calcular_desconto`. Não precisa de navegador nem de preparação, porque é um teste unitário.
- **Resultado esperado:** a função retorna 10, que é 10% de 100. Ela devolve só o valor do desconto, não o valor final do pedido.
- **O que faria o teste falhar:** se a condição da função fosse `valor_pedido > 100` em vez de `valor_pedido >= 100`, o pedido de R$ 100,00 não receberia desconto, a função retornaria 0 e o `assert resultado == 10` falharia.

---

## 8. Uso de inteligência artificial

O uso de inteligência artificial é permitido como apoio, mas todo o conteúdo e código devem ser revisados, executados e compreendidos pela equipe.

- **Ferramenta utilizada:** Claude
- **Como a ferramenta foi utilizada:** como apoio e guia durante a atividade. Usei para entender o fluxo do TDD e do Playwright e para receber sugestões de estrutura dos testes e dos locators. Escrevi a função `calcular_desconto`, executei os testes a cada etapa (Red e Green) e ajustei o código conforme os resultados do pytest.
- **Uma sugestão que precisou ser alterada ou rejeitada:** a sugestão de usar `get_by_text("Restaurante Sabor 0", exact=True)` na assertion do teste funcional. Ela falhou com "element(s) not found".
- **Motivo da alteração ou rejeição:** cada restaurante é exibido como um link com nome, preço, categoria e bairro juntos, então o texto exato não correspondia a nenhum elemento. Troquei por `get_by_role("link").filter(has_text=...)`, que conta os cards de cada categoria. Também precisei acrescentar a espera da lista carregar antes do clique.
- **Como o código sugerido foi verificado:** executei todos os testes com `python -m pytest -v`, acompanhei cada falha e aprovação no terminal, conferi no site os restaurantes de cada categoria e gerei o `relatorio-pytest.txt` com 5 testes aprovados.
---

## 9. Diferenciais opcionais

Marque somente os diferenciais realmente implementados e inclua ao lado os respectivos links.

- [x] Terceiro teste unitário para caso de borda.
- [x] Uso de `pytest.raises` para verificar exceção.
- [ ] Parametrização com `pytest.mark.parametrize`.
- [ ] Cenário BDD em Gherkin.
- [ ] Automação com `pytest-bdd`.
- [ ] Organização com Page Object Model.
- [ ] Segundo teste funcional pelo mesmo integrante.
- [ ] Execução em mais de um navegador.
- [ ] Screenshot, vídeo ou trace do Playwright.
- [ ] Registro de uma falha encontrada e corrigida.

### Descrição dos diferenciais

- **Caso de borda:** `test_pedido_de_100_recebe_desconto_de_10` em `tests/test_regras_localeats.py` verifica o valor exato de R$ 100,00, que é o limite da regra de desconto.
- **`pytest.raises`:** `test_valor_negativo_gera_value_error` em `tests/test_regras_localeats.py` verifica que um valor negativo gera `ValueError`.
- **Falha encontrada e corrigida:** no `TF01` (`tests/test_localeats.py`), o teste falhou por timeout porque o Playwright abre sem sessão e o site redirecionava para `login.html`. Corrigi adicionando o login no início do teste. Depois, a assertion falhou porque o clique em "Italiana" ocorreu antes da lista carregar. Corrigi esperando o primeiro card aparecer antes de clicar.

---