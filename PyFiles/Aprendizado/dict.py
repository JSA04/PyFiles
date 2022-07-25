import os

os.system("cls")

dicionario = { "KEY1" : 100,
               "KEY2" : 200,
               "KEY3" : 300 }

#######################################################################################################

values = [value for value in dicionario.values()]

i = 1

print(f"{i} : 'values()' possibilita a iteração apenas nos valores do dicionario.\n"
      f"[value for value in dicionario.values()] : \033[31m{values}\033[m\n")
i+=1

#######################################################################################################

keys = [key for key in dicionario.keys()]

print(f"{i} - 'keys()' possibilita a iteração apenas nas chaves do dicionario.\n"
      f"[key for key in dicionario.keys()] : \033[31m{keys}\033[m\n")
i+=1

#######################################################################################################

get = dicionario.get("KEY1")

print(f"{i} - 'get()' retorna o valor da chave que passamos.\n"
      f"dicionario.get('KEY1') : \033[31m{get}\033[m\n")
i+=1

#######################################################################################################

items = [[chave, valor] for chave, valor in dicionario.items()]

print(f"{i} - 'items()' possibilita a iteração pela chave e o valor ao mesmo tempo.\n"
      f"[[chave, valor] for chave, valor in dicionario.items()] : \033[31m{items}\033[m\n")
i+=1

#######################################################################################################

pop = dicionario.pop("KEY1")

print(f"{i} - 'pop()' retorna o valor e apaga o item que contem a chave que passamos.\n"
      f"dicionario.pop('KEY1') : \033[31m{pop}\033[m\n"
      f"dicionario : \033[31m{dicionario}\033[m\n")
i+=1

#######################################################################################################

popitem = dicionario.popitem()

print(f"{i} - 'popitem()' retorna o valor e apaga o ultimo item do dicionario.\n"
      f"dicionario.popitem() : \033[31m{popitem}\033[m\n"
      f"dicionario : \033[31m{dicionario}\033[m\n")
i+=1

#######################################################################################################

dicionario_copy = dicionario.copy()

print(f"{i} - 'copy()' retorna uma cópia do dicionario.\n"
      f"dicionario_copy = dicionario.copy() : \033[31m{dicionario_copy}\033[m\n")
i+=1

#######################################################################################################

clear = dicionario.clear()

print(f"{i} - 'clear()' limpa todo o dicionario.\n"
      f"dicionario : \033[31m{dicionario}\033[m\n")
i+=1

#######################################################################################################

setdefault = dicionario.setdefault("KEY4", 400)

print(f"{i} - 'setdefault()' retorna o valor da chave especificada caso ela exista, caso contrario é "
      f"criado um novo item com essa chave e com o valor especificado.\n"
      f"dicionario.setdefault('KEY4', 400) : \033[31m{setdefault}\033[m\n"
      f"dicionario : \033[31m{dicionario}\033[m\n")
i+=1

#######################################################################################################

update = dicionario.update({"KEY4": 500})

print(f"{i} - 'update()' atualiza o dicionario, adicionando se não existe a chave ou mudando o valor "
      f"caso a chave exista.\n"
      "dicionario.update({'KEY4': 500}\n"
      f"dicionario : \033[31m{dicionario}\033[m\n")
i+=1

#######################################################################################################

lista1 = ["KEY1", "KEY2"]
lista2 = [100, 200]

dict_zip = dict(zip(lista1, lista2))

print(f"{i} - 'dict(zip())' consegue transformar 2 listas em um dicionario, os items da primeira lista serão "
      f"as chaves e as da segunda serão os valores, considerando a posição deles.\n"
      f"dict(zip(lista1, lista2)) - \033[31m{dict_zip}\033[m")
i+=1
