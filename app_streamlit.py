import streamlit as st
import requests

st.title("Calculadora de Financiamento")

# Entradas do usuário
# Usando text_input o usuário pode realmente apagar e deixar vazio
valor_str = st.text_input("Valor do produto (R$)", value="")
taxa_str = st.text_input("Taxa de Juros mensal (%)", value="")
meses_str = st.text_input("Prazo (meses)", value="")

if st.button("Calcular Financiamento"):
    # Convertemos para float/int apenas se houver valor, senão mandamos vazio ou 0 para a API validar
    params = {
        "valor": float(valor_str) if valor_str else 0.0,
        "taxa_juros": float(taxa_str) if taxa_str else -1.0, # ou o valor que dispara sua regra
        "meses": int(meses_str) if meses_str else 0
    }
    
    response = requests.post("https://calculadora-de-financiamento.onrender.com/Calculadora", params=params)
    resultado = response.json()
    
    if "erro" in resultado:
        st.error(resultado["erro"])
    else:
        st.success("Cálculo realizado com sucesso!")
        st.metric("Parcela Mensal", f"R$ {resultado['Parcela mensal']}")
