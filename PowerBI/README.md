# Desafio de Projeto: Modelo Star Schema no Power BI

Este repositório contém a solução para o desafio de projeto de construção de um modelo baseado em star schema utilizando o Power BI. Abaixo, detalhamos o passo a passo do processo, as etapas do projeto, as funcionalidades e as funções DAX utilizadas.

## Objetivo do Desafio

Criar um modelo star schema a partir de uma tabela única chamada **Financial Sample**. O projeto envolve a criação de tabelas dimensão e fato com base na tabela original, utilizando recursos de modelagem e cálculos no Power BI.

## Estrutura do Projeto

O projeto consiste na criação das seguintes tabelas:

- **Financials_origem**: Tabela original utilizada como backup (modo oculto).
- **D_Produtos**: Contém informações sobre produtos e estatísticas de vendas.
- **D_Produtos_Detalhes**: Detalhes adicionais sobre produtos.
- **D_Descontos**: Informações sobre descontos aplicados.
- **D_Detalhes**: Informações complementares não contempladas nas demais tabelas.
- **D_Calendário**: Tabela de calendário criada com a função DAX `CALENDAR()`.
- **F_Vendas**: Tabela fato consolidando informações de vendas.

---

## Passo a Passo da Construção

### 1. Configuração Inicial
1. Importar a tabela **Financial Sample** para o Power BI.
2. Renomear a tabela importada para **Financials_origem** e definir como oculta para evitar alterações diretas.

### 2. Criação das Tabelas Dimensão

#### a) **D_Produtos**
1. Duplicar a tabela **Financials_origem** e renomear para **D_Produtos**.
2. Selecionar as colunas:
   - `ID_produto`
   - `Produto`
3. Criar as seguintes métricas utilizando DAX:
   - **Média de Unidades Vendidas:** `AVERAGE(Units Sold)`
   - **Média do Valor de Vendas:** `AVERAGE(Sales)`
   - **Mediana do Valor de Vendas:** `MEDIAN(Sales)`
   - **Valor Máximo de Venda:** `MAX(Sales)`
   - **Valor Mínimo de Venda:** `MIN(Sales)`

#### b) **D_Produtos_Detalhes**
1. Criar uma nova tabela e incluir as colunas:
   - `ID_produto`
   - `Discount Band`
   - `Sale Price`
   - `Units Sold`
   - `Manufacturing Price`

#### c) **D_Descontos**
1. Duplicar a tabela original e selecionar as colunas:
   - `ID_produto`
   - `Discount`
   - `Discount Band`

#### d) **D_Detalhes**
1. Criar uma tabela para armazenar informações adicionais de vendas não contempladas nas demais tabelas.

#### e) **D_Calendário**
1. Criar uma tabela de calendário com a função DAX:
   ```DAX
   D_Calendário = CALENDAR(MIN(Financials_origem[Date]), MAX(Financials_origem[Date]))
   ```

### 3. Criação da Tabela Fato (**F_Vendas**)
1. Criar uma nova tabela consolidando os dados essenciais de vendas:
   - `SK_ID`
   - `ID_Produto`
   - `Produto`
   - `Units Sold`
   - `Sales Price`
   - `Discount Band`
   - `Segment`
   - `Country`
   - `Salers`
   - `Profit`
   - `Date`

### 4. Modelagem do Diagrama
1. Reorganizar as tabelas no modelo de dados para formar o esquema estrela:
   - A tabela **F_Vendas** no centro.
   - As tabelas dimensão conectadas a ela via chaves estrangeiras.
2. Definir os relacionamentos apropriados entre as tabelas.

---

## Funções DAX Utilizadas

- `AVERAGE()`: Cálculo da média.
- `MEDIAN()`: Cálculo da mediana.
- `MAX()`, `MIN()`: Identificação dos valores máximo e mínimo.
- `CALENDAR()`: Criação da tabela de calendário.

---

## Salvar e Documentar o Projeto

1. Salvar o arquivo **.pbix**.
2. Exportar uma imagem do diagrama de esquema em estrela.
3. Subir o projeto para um repositório no GitHub com o README.md explicativo.

---

## Exemplo de Repositório

Inclua neste repositório:
- Arquivo **.pbix**.
- Imagem do esquema em estrela.
- Este README.md detalhado.

Com isso, temos a solução do desafio pronta para compartilhar com a comunidade.
