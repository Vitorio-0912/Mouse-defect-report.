contador_total = 0
contador_sit_1 = 0
contador_sit_2 = 0
contador_sit_3 = 0
contador_sit_4 = 0 

indentificador = (input("Informe a indentificação: ")) #sem int para o usuário se indentificar com o nome ou número.

while indentificador != 0:
    print("1 - Necessidade de esfera.")
    print("2 - Necessidade de limpeza.")
    print("3 - Necessidade troca do cabo ou conector.")
    print("4 - Quebrado ou inultilizado.")
    defeito = int(input("Informe o tipo de defeito: "))

    if defeito == 1:
        contador_sit_1 = contador_sit_1 + 1
    elif defeito == 2:
        contador_sit_2 = contador_sit_2 + 1
    elif defeito == 3:
        contador_sit_3 = contador_sit_3 + 1
    elif defeito == 4:
        contador_sit_4 = contador_sit_4 + 1
    contador_total = contador_total + 1
    indentificador = int(input("Informe a Indentifação: "))

p1 = contador_sit_1 / contador_total * 100.0
p2 = contador_sit_2 / contador_total * 100.0
p3 = contador_sit_3 / contador_total * 100.0
p4 = contador_sit_4 / contador_total * 100.0
print("Quantidade de mouses: {0}".format(contador_total))

print("Situação                                    Quantidade                      Percentual")
print("1 - necessidade de esfera                          {0}                        {1:.2f}%".format(contador_sit_1, p1))
print("2 - necessidade de limpeza                         {0}                        {1:.2f}%".format(contador_sit_1, p1))
print("3 - necessidade troca do cabo ou conector          {0}                        {1:.2f}%".format(contador_sit_1, p1))
print("4 - Quebrado ou inultilizado                       {0}                        {1:.2f}%".format(contador_sit_1, p1))
        

