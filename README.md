# Projeto Final: Análise de Dados e Fundamentos de IA 🚗🤖

Este repositório contém o projeto final focado na criação, treinamento e deploy de um modelo de Machine Learning para a estimativa de preços de veículos. O projeto contempla desde a construção de uma API robusta em Python até uma interface web moderna e intuitiva para o usuário final.

---

## 🚀 Demonstração & Links Úteis

- **URL do Deploy (API):** (https://carrovalor.lovable.app/))
- **Interface Web:** Desenvolvida integrada ao modelo preditivo.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem Principal:** Python 3
- **Framework Web (API):** Flask
- **Segurança & Integração:** Flask-CORS (Cross-Origin Resource Sharing)
- **Inteligência Artificial:** Scikit-Learn (`LinearRegression`)
- **Manipulação de Dados:** Pandas
- **Banco de Dados / Backend BaaS:** Supabase (`supabase-py`)
- **Gerenciamento de Variáveis de Ambiente:** Python-dotenv
- **Servidor de Produção WSGI:** Gunicorn
- **Ferramentas de Teste:** Postman
- **Hospedagem/Deploy:** Render
- **Interface Base:** Lovable (Frontend integrado)
---

## 📦 Estrutura e Funcionalidades

### 1. Interface do Usuário (Frontend)
Uma aplicação web intuitiva onde o usuário pode selecionar as especificações do veículo, como:
- Ano do veículo
- Quilometragem
- Motorização (ex: 1.4, 2.0)
- Número de revisões feitas
- Cor do Ford GT40

O modelo de Machine Learning analisa os dados em tempo real e retorna a estimativa de valor em segundos.

### 2. API Backend (Flask + IA + Supabase)
O coração do projeto é uma API Flask que:
- Permite requisições de diferentes origens de forma segura usando **CORS**.
- Utiliza **Variáveis de Ambiente (`.env`)** para proteger credenciais confidenciais de banco de dados.
- Conecta-se ao banco de dados **Supabase** para buscar ou persistir dados estruturados.
- Processa os dados com **Pandas** e alimenta o modelo de **Regressão Linear** para gerar previsões de preço de forma instantânea.

### 3. Deploy em Produção (Render)
A aplicação está totalmente funcional e hospedada na nuvem através do **Render**, utilizando contêineres e gerenciamento automatizado de processos com Gunicorn e concorrência web ajustada nativamente.

---

## 📸 Demonstrações Visuais (Screenshots)

### Interface de Avaliação de Veículos
*Layout limpo e moderno focado na experiência do usuário para descobrir o preço estimado do veículo.*
<img width="1024" height="456" alt="image" src="https://github.com/user-attachments/assets/e668ef76-72a1-4b79-aab1-9165136fff93" />

### API Backend em Execução (Local)
*Servidor Flask rodando localmente com suporte a logs detalhados e recebendo requisições do tipo POST.*
<img width="835" height="204" alt="image" src="https://github.com/user-attachments/assets/05ab1678-b133-41f4-89b8-08da21e05e4e" />

### Testes de Requisição com Postman
*Validação do endpoint `/prever` enviando um JSON com os atributos do veículo e recebendo o preço predito de forma instantânea.*
<img width="1485" height="648" alt="image" src="https://github.com/user-attachments/assets/98baa54f-a6ab-4bc3-883b-9093a159a440" />

### Dashboard de Deploy (Render)
*Logs de execução da instância em produção no Render mostrando o serviço Live e rodando via Gunicorn.*
<img width="1522" height="820" alt="image" src="https://github.com/user-attachments/assets/a4d68bbe-30f3-4b51-916e-f0d0e3b1d97f" />

---

## 🔧 Como Executar o Projeto Localmente

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/rafzsxl/ProjetoFinal-An-lise-Dados-e-Fundamentos_IA.git](https://github.com/rafzsxl/ProjetoFinal-An-lise-Dados-e-Fundamentos_IA.git)
   cd ProjetoFinal-An-lise-Dados-e-Fundamentos_IA
