# Atividade 4: Testes Automatizados do LocalEats

> **Orientação:** substitua os textos entre colchetes pelas informações da equipe. Remova as orientações que não fizerem parte da entrega final.

---

## 1. Identificação

- **Turma:** [ADS5N26-2C]
- **Modalidade:** [Individual]
- **Repositório:** [[Repositório Github](https://github.com/tatomachadodev/localeats-qualidade)]
- **Diretório da atividade:** [colar o link direto para este diretório]
- **Data da última execução:** [dd/mm/aaaa]

### Integrantes

1. [Nome completo]
2. [Nome completo, se houver]
3. [Nome completo, se houver]
4. [Nome completo, se houver]

---

## 2. Integrantes e responsabilidades

Preencha uma linha para cada teste. Os testes unitários devem usar identificadores `TU01`, `TU02` e seguintes. Os testes funcionais devem usar `TF01`, `TF02` e seguintes.

| ID | Integrante responsável | Tipo | Comportamento verificado | Arquivo e função de teste |
|---|---|---|---|---|
| TU01 | [nome] | Unitário | [comportamento] | `tests/test_regras_localeats.py::test_nome` |
| TU02 | [nome] | Unitário | [comportamento] | `tests/test_regras_localeats.py::test_nome` |
| TF01 | [nome] | Funcional | [comportamento] | `tests/test_localeats.py::test_nome` |

> Adicione as linhas necessárias conforme a quantidade de integrantes.

### Quantidades mínimas

- **Individual:** uma função, dois testes unitários e um teste funcional.
- **Dupla:** duas funções, quatro testes unitários e dois testes funcionais.
- **Trio:** três funções, seis testes unitários e três testes funcionais.
- **Equipe de quatro:** quatro funções, oito testes unitários e quatro testes funcionais.

Cada teste funcional deve possuir pelo menos duas assertions. Integrantes da mesma equipe devem escolher regras e fluxos diferentes.

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

#### Regra de [nome do integrante]

- **Regra escolhida:** [informar]
- **Função implementada:** `[nome da função]`
- **Arquivo da implementação:** [`src/regras_localeats.py` ou outro caminho]
- **Testes criados:** [`nome do primeiro teste`; `nome do segundo teste`]
- **Comportamentos verificados:** [descrever brevemente]

> Repita esta subseção para cada integrante.

---

## 4. Aplicação do TDD

Cada integrante deve registrar de forma breve o desenvolvimento orientado a testes da própria regra.

### TDD de [nome do integrante]

- **Regra escolhida:** [informar]
- **Primeiro teste escrito:** `[nome da função de teste]`
- **Por que o teste falhou inicialmente:** [explicar]
- **Implementação mínima realizada:** [explicar]
- **Segundo teste escrito:** `[nome da função de teste]`
- **Melhoria ou refatoração realizada:** [explicar ou informar que não foi necessária]

> Repita esta subseção para cada integrante.

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

### Teste funcional de [nome do integrante]

- **ID:** `TF01`
- **Fluxo automatizado:** [descrever]
- **Interação realizada:** [descrever]
- **Primeira assertion:** [descrever o resultado verificado]
- **Segunda assertion:** [descrever o resultado verificado]
- **Arquivo e função:** `tests/test_localeats.py::test_nome`
- **Resultado final:** [aprovado / reprovado]

> Repita esta subseção para cada integrante.

---

## 6. Resultado da execução

Execute todos os testes no PowerShell:

```powershell
python -m pytest -v | Tee-Object -FilePath relatorio-pytest.txt
```

Depois, registre o resultado:

- **Quantidade total de testes:** [informar]
- **Testes aprovados:** [informar]
- **Testes reprovados:** [informar]
- **Link para o relatório:** [relatorio-pytest.txt](relatorio-pytest.txt)
- **Observações:** [informar falhas conhecidas ou escrever “Todos os testes foram aprovados”]

---

## 7. Explicações individuais

Cada integrante deve escolher um teste de sua responsabilidade e demonstrar compreensão sobre o código entregue.

### Explicação do teste de [nome do integrante]

- **Teste escolhido:** `[nome da função de teste]`
- **Comportamento verificado:** [explicar]
- **Dados ou estado inicial:** [explicar]
- **Resultado esperado:** [explicar]
- **O que faria o teste falhar:** [explicar]

> Repita esta subseção para cada integrante.

---

## 8. Uso de inteligência artificial

O uso de inteligência artificial é permitido como apoio, mas todo o conteúdo e código devem ser revisados, executados e compreendidos pela equipe.

- **Ferramenta utilizada:** [informar ou escrever “Não utilizada”]
- **Como a ferramenta foi utilizada:** [informar]
- **Uma sugestão que precisou ser alterada ou rejeitada:** [informar]
- **Motivo da alteração ou rejeição:** [informar]
- **Como o código sugerido foi verificado:** [informar testes, execução e revisão realizados]

---

## 9. Diferenciais opcionais

Marque somente os diferenciais realmente implementados e inclua ao lado os respectivos links.

- [ ] Terceiro teste unitário para caso de borda.
- [ ] Uso de `pytest.raises` para verificar exceção.
- [ ] Parametrização com `pytest.mark.parametrize`.
- [ ] Cenário BDD em Gherkin.
- [ ] Automação com `pytest-bdd`.
- [ ] Organização com Page Object Model.
- [ ] Segundo teste funcional pelo mesmo integrante.
- [ ] Execução em mais de um navegador.
- [ ] Screenshot, vídeo ou trace do Playwright.
- [ ] Registro de uma falha encontrada e corrigida.

### Descrição dos diferenciais

[Descreva os diferenciais implementados e informe os arquivos correspondentes. Remova esta seção caso nenhum diferencial tenha sido desenvolvido.]

---