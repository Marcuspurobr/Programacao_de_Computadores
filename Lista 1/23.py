print('Aluno: XXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nNro Matrícula: XXXXXXXXXXX\n-------------------------------------\nPrograma referente ao exercício 23\n-------------------------------------',)
vendas = float(input('Insira quantos reais foram de vendas: '))
comissao = float(input('Insira o valor da comissão (em porcentagem[número de 1 a 100]): '))
comissaototal = (vendas*comissao)/100
round(comissaototal)
comissaototal_formatado = "{:.2f}".format(comissaototal)
vendas_formatado = "{:.2f}".format(vendas)
linha1 = (' ------------------------------------------------------- ')
linha2 = ('|                  Vendas de Agosto                     |')
linha3 = (f'| Total vendas:   R$ {vendas_formatado}')
linha4 = (f'| Comissão:       R$ {comissaototal_formatado}')
linha5 = (' ------------------------------------------------------- ')
espacos3 = 35-len(str(vendas_formatado))
espacos4 = 35-len(str(comissaototal_formatado))
print(linha1)
print(linha2)
print(linha3+(' ')*espacos3+('|'))
print(linha4+(' ')*espacos4+('|'))
print(linha5)
print('-------------------------------------')
