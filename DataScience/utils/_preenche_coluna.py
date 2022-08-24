def preenche_coluna(cls, coluna_a_preencher, valores_a_usar):
    try:
        cls.df[coluna_a_preencher]

    except KeyError:
        print(f"Não há colunas com o nome {coluna_a_preencher}")

    else:
        if len(valores_a_usar) == cls.qtd:
            cls.df[coluna_a_preencher] = valores_a_usar
        else:
            print("Não foi possivel preencher a coluna")

            if len(valores_a_usar) > cls.get_qtd:
                print(f"{len(valores_a_usar)} > {cls.get_qtd}")
                
            elif len(valores_a_usar) < cls.get_qtd:
                print(f"{len(valores_a_usar)} < {cls.get_qtd}")
