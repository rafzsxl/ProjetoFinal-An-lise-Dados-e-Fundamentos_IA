# Projeto de Previsão de Valor de Carros Usados

## Visão geral👀👀

Este projeto tem como objetivo prever o valor de um carro usado com base em características importantes do veículo, como:

- ano de fabricação
- quilometragem
- tamanho do motor
- quantidade de revisões

A ideia é transformar esses dados em uma estimativa de preço, permitindo que o usuário tenha uma referência rápida e prática para avaliar o valor de um automóvel.

---

## Como o projeto funciona🤷‍♂️

O projeto é composto por uma API desenvolvida em Python utilizando Flask. A aplicação faz o seguinte:

1. Carrega um dataset com informações de carros usados.
2. Seleciona as variáveis que serão usadas para treinar o modelo.
3. Treina um modelo de Machine Learning chamado Regressão Linear.
4. Expondo uma API para receber dados e retornar uma previsão de preço.

Em termos simples, o modelo aprende a relação entre as características do carro e o preço, e depois consegue estimar o valor de um novo carro a partir dessas informações.

---

## Como foi feito este projeto🔎🔎🔎

O projeto foi construído com uma abordagem simples e objetiva:

- O dataset foi carregado com a biblioteca pandas.
- O modelo de predição foi treinado com scikit-learn.
- A API foi criada com Flask.
- O CORS foi habilitado para permitir que o frontend consiga consumir a API.

Essa estrutura é bastante comum em projetos de IA e automação, pois separa bem a parte de dados, o modelo e a interface de acesso.

---

## O que foi utilizado⚒️

### Tecnologias e bibliotecas

- Python
- Flask
- Flask-CORS
- pandas
- scikit-learn

### Conceitos breves utilizados

- Regressão Linear: técnica de Machine Learning usada para prever valores contínuos, como preços.
- Features: são as entradas do modelo, ou seja, as características utilizadas para fazer a previsão.
- Target: é o valor que o modelo tenta prever, neste caso o preço do carro.
- API: é uma interface que permite que outras aplicações, como sites e aplicativos, enviem dados e recebam respostas automaticamente.

---

## Estrutura do projeto🏠

- app.py: arquivo principal com a API e o modelo treinado.
- dataset_carros_usados_2.csv: arquivo com os dados usados para treinar o modelo.
- requirements.txt: dependências do projeto.

---

## Como usar o projeto

### 1. Instale as dependências

No terminal, dentro da pasta do projeto, execute:

```bash
pip install -r requirements.txt
```

### 2. Execute a aplicação

```bash
python app.py
```

A API ficará disponível localmente em:

```text
http://127.0.0.1:8000
```

---

## Como consumir a API

### Endpoint GET

O endpoint raiz verifica se a API está online.

```bash
curl http://127.0.0.1:8000/
```

Resposta esperada:

```json
{
  "Resposta": "API online, Flask rodando corretamente"
}
```

### Endpoint POST

Para fazer uma previsão, envie um JSON para o endpoint /prever com os campos abaixo:

```json
{
  "ano": 2018,
  "quilometragem": 50000,
  "motor": 2.0,
  "num_revisoes": 3
}
```

Exemplo com curl:

```bash
curl -X POST http://127.0.0.1:8000/prever \
  -H "Content-Type: application/json" \
  -d '{"ano": 2018, "quilometragem": 50000, "motor": 2.0, "num_revisoes": 3}'
```

Resposta esperada:

```json
{
  "preco": 65000.0
}
```

---

## Para que este projeto pode ser usado

Este projeto pode ser utilizado para:

- estimar o valor de um carro usado
- criar uma ferramenta de avaliação automotiva
- integrar com sites ou sistemas que precisam de uma avaliação rápida
- servir como base para projetos mais avançados de Machine Learning

Ele é especialmente útil em contextos de marketplaces, plataformas de compra e venda e aplicações voltadas ao setor automotivo.

---

## Links importantes

- API (método GET): https://projetofinal-an-lise-dados-e-fundamentos.onrender.com/
- API (método POST): https://projetofinal-an-lise-dados-e-fundamentos.onrender.com/prever
- Site: https://carrovalor.lovable.app/

---

## Observação final

Este projeto mostra como é possível combinar dados, Machine Learning e uma API em uma solução simples, útil e de fácil entendimento. O objetivo não é apenas prever preços, mas também demonstrar como um modelo pode ser colocado em produção para ser consumido por diferentes aplicações.
