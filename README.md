Calculadora de Financiamento API

API desenvolvida com FastAPI para realizar cálculos de financiamento de forma rápida e segura. O sistema conta com documentação interativa integrada e validação automática de dados.
🚀 Tecnologias Utilizadas

    Python

    FastAPI

    Uvicorn

📋 Pré-requisitos

Certifique-se de ter o Python instalado em sua máquina. Você também precisará instalar as dependências do projeto:

pip install fastapi uvicorn

⚙️ Como Executar o Projeto

    Clone este repositório ou abra a pasta do projeto no seu editor de código (como o VS Code).

    Inicie o servidor da API utilizando o Uvicorn através do terminal:

    uvicorn main:app --reload

    O servidor estará rodando localmente em: http://127.0.0.1:8000/docs.

🔌 Exemplo de Uso (Rota)

POST /Calculadora
Realiza o cálculo com base nos parâmetros enviados:

    Parâmetros de Consulta (Query Params):

        valor (número): Valor total do financiamento.

        taxa_juros (número): Taxa de juros aplicada.

        meses (inteiro): Prazo total em meses.

Projeto construído para estudos e aplicação prática de desenvolvimento de APIs modernas com Python.