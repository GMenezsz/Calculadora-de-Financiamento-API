import streamlit as st
import requests

st.title("Calculadora de Financiamento")

# Entradas do usuário
valor = st.number_input("Valor do produto (R$)", min_value=0.01, step=100.0)
taxa = st.number_input("Taxa de Juros mensal (%)", min_value=0.0, step=0.1)
meses = st.number_input("Prazo (meses)", min_value=1, step=1)

if st.button("Calcular Financiamento"):
    # Parâmetros que a sua API espera
    params = {
        "valor": valor,
        "taxa_juros": taxa,
        "meses": meses
    }
    
    # Fazendo a requisição para a sua API local
    # Note que usamos 'params=' para enviar via query string
    try:
        response = requests.post("http://localhost:8000/Calculadora", params=params)
        resultado = response.json()
        
        # Verifica se deu erro ou se tem o resultado
        if "erro" in resultado:
            st.error(resultado["erro"])
        else:
            st.success("Cálculo realizado com sucesso!")
            # Exibe os resultados bonitinhos
            st.metric("Parcela Mensal", f"R$ {resultado['Parcela mensal']}")
            st.metric("Valor Total", f"R$ {resultado['Valor total']}")
            st.metric("Total de Juros", f"R$ {resultado['Valor total de juros']}")
            
    except Exception as e:
        st.error("Não foi possível conectar ao servidor. Certifique-se de que o FastAPI está rodando!")
