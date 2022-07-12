import matplotlib.pyplot as plt

x = ["Janeiro",  "Feveriro", "Maio",     "Abril",
     "Março",    "Junho",    "Julho",    "Agosto",
     "Setembro", "Outubro",  "Novembro", "Dezembro"]    # Valores da Linha

y = [20, 10, 70, 80, 20, 10, 5, 0, 10, 0, 0, 10]    # Valores da Coluna

plt.plot(x, y, marker="o")
plt.title("Chuvas em cada mês")
plt.xlabel('Mês')
plt.ylabel("Milimetros")
plt.show()
