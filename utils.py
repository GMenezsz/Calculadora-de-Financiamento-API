def calculadora(valor, taxa_juros, meses):
    valor_produto = valor
    juros_mensal = taxa_juros / 100
    prazo = int(meses)

    fator = (1 + juros_mensal) ** prazo

    parcela_mensal = (valor_produto * (fator * juros_mensal)) / (fator - 1)

    valor_total = parcela_mensal * prazo
    total_juros = valor_total - valor_produto

    return {
        "Parcela mensal": round(parcela_mensal, 2),
        "Valor total": round(valor_total, 2),
        "Valor total de juros": round(total_juros, 2),
        }

def validar_valor(valor):
    if valor <= 0:
        return False
    else:
        return True

def validar_juros(taxa_juros):
    if taxa_juros < 0:
        return False
    else:
        return True

def validar_prazo(meses):
    if meses < 1:
        return False
    else: 
        return True