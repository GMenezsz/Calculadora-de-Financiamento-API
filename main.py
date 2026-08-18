from fastapi import FastAPI
from utils import calculadora, validar_valor, validar_juros, validar_prazo

app = FastAPI(title="Calculadora de Financiamento")

@app.post("/Calculadora")
def api_calculadora(valor: float, taxa_juros: float, meses: int):

    valor_produto = valor
    resultado_valor = validar_valor(valor_produto)

    taxa = taxa_juros
    resultado_taxa = validar_juros(taxa)

    prazo = meses
    resultado_prazo = validar_prazo(prazo)


    if resultado_valor is not True:
        return {"erro": "O valor deve ser maior do que 0."}

    elif resultado_taxa is not True:
        return {"erro": "O campo da taxa de juros não pode ser negativo."}

    elif resultado_prazo is not True:
        return {"erro": "O campo do prazo não pode ser negativo."}
    else:
        return calculadora(valor_produto, taxa, prazo)
