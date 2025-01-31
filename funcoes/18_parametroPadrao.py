def calculo_gasto_combustivel(km_percorrido, valor_combustivel, media_km_veiculo=9.5):
    valor_total = (km_percorrido / media_km_veiculo) * valor_combustivel
    return valor_total


kms = 350
valor_gasolina = 5.59
media_veiculo = 12
resultado_com_media_padrao = calculo_gasto_combustivel(kms, valor_gasolina)

resultado_com_media = calculo_gasto_combustivel(kms, valor_gasolina, media_veiculo)

print(f"Resultado com média padrão: {resultado_com_media_padrao:.2f}")
print(f"REsultado sem média padrão: {resultado_com_media:.2f}")
