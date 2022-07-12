def verifica(palavra: list):
    palavra_str = palavra[0]
    caracteres_invalidos = "-_áãâà.éèêóòôõìíìúîùç "
    for caracter in caracteres_invalidos:
        if caracter in palavra_str or len(palavra_str) != 5:
            return False
    return True


with open("C:/Users/f72823/Documents\Py\Codes\Palavras\palavras.txt", encoding="UTF-8") as arq:
    palavras_str = arq.readline().replace(" ", ";")
    index = 0
    lista_palavras = []

    for letra in palavras_str:

        if letra != ";":
            if not lista_palavras:
                lista_palavras.append([])

            if not lista_palavras[index]:
                lista_palavras[index] += letra

            else:
                lista_palavras[index][0] += letra

        elif letra == ";":
            lista_palavras.append(list())
            index += 1
    arq.close()


print(lista_palavras)

palavras = list()

for palavra in lista_palavras:
    if verifica(palavra):
        palavras.append(palavra)
