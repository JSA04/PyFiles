# O MAP aplica uma função em cada item de uma lista
precos = [1000, 1500, 1250, 2500]


# Função que adiciona imposto
def adiciona_imposto(valor):
    return valor * 1.1


# Aplicando uma função em cada item de uma lista usando FOR
precos_com_imposto = []

for preco in precos:
    precos_com_imposto.append(adiciona_imposto(preco))

print(f"Com FOR: {precos_com_imposto}")

# Aplicando uma função em cada item de uma lista usando MAP
precos_com_imposto2 = list(map(adiciona_imposto, precos))

print(f"Com MAP: {precos_com_imposto2}")
