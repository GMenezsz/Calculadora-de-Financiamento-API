import streamlit as st
import requests

st.title("Calculadora de Financiamento")

# Campos de texto para o usuário digitar livremente (ex: 50.000,00 ou 40000)
valor_str = st.text_input("Valor do produto (R$)", value="")
taxa_str = st.text_input("Taxa de Juros mensal (%)", value="")
meses_str = st.text_input("Prazo (meses)", value="")

def limpar_numero(texto):
    if not texto:
        return 0.0
    # Remove os pontos de milhar e substitui a vírgula decimal por ponto
    texto_limpo = texto.replace(".", "").replace(",", ".")
    try:
        return float(texto_limpo)
    except ValueError:
        return 0.0

def formatar_br(valor):
    # Formata no padrão brasileiro (ponto para milhares, vírgula para decimais)
    return f"{valor:,.2f}".replace(",", "_").replace(".", ",").replace("_", ".")

if st.button("Calcular Financiamento"):
    # Limpa e converte os valores digitados
    valor = limpar_numero(valor_str)
    taxa_juros = limpar_numero(taxa_str)
    
    # Para os meses (inteiro), removemos qualquer ponto ou vírgula caso digitem
    meses_limpo = meses_str.replace(".", "").replace(",", "")
    meses = int(meses_limpo) if meses_limpo.isdigit() else 0

    params = {
        "valor": valor,
        "taxa_juros": taxa_juros,
        "meses": meses
    }
    
    try:
        response = requests.post("https://calculadora-de-financiamento.onrender.com/Calculadora", params=params)
        resultado = response.json()
        
        if "erro" in resultado:
            st.error(resultado["erro"])
        else:
            st.success("Cálculo realizado com sucesso!")
            st.metric("Parcela Mensal", f"R$ {formatar_br(resultado['Parcela mensal'])}")
            st.metric("Valor Total", f"R$ {formatar_br(resultado['Valor total'])}")
            st.metric("Total de Juros", f"R$ {formatar_br(resultado['Valor total de juros'])}")
            
    except Exception as e:
        st.error(f"Erro de conexão: {e}")
