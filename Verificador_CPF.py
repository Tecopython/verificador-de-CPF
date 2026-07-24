def confere(cpf:list):
    cpf_c = cpf[0:9]
    somador = 0
    contador = 10
    for n in cpf_c:
        somador += n*contador
        contador -= 1
    resto = somador % 11
    if resto == 0 or resto == 1:
        cpf_c.append(0)
    else:
        cpf_c.append(11 - resto)
    
    somador = 0
    contador = 11
    for n in cpf_c:
        somador += n*contador
        contador -= 1
    resto = somador % 11
    if resto == 0 or resto == 1:
        cpf_c.append(0)
    else:
        cpf_c.append(11 - resto)
    
    if cpf == cpf_c:
        return True
    else:
        return False

def mostra_cpf(cpf:list):
    concat = ''
    contador = 1
    for x in cpf:
        if contador % 3 == 0 and contador != 9:
            concat+= str(x)
            concat += '.'
            contador += 1
        else:
            concat += str(x)
            contador += 1
        if contador == 10:
            concat += '-'
    return concat






while True:
    try:
        cpf = input('Digite o CPF (sem "." e e sem "-") --> ')
        cpf = [int(x) for x in cpf]
        if len(cpf) > 11:
            print('Você colocou números demais, revise')
            continue
        elif len(cpf) < 11:
            print('Está faltando números, confira novamente')
            continue
        else:
            break
    except ValueError as v:
        print(f'Você não digitou um número válido')
    except KeyboardInterrupt:
        print("Usuário desconectou pelo teclado")
        break

#realizar as contas
try:

    if confere(cpf):
            print(f'O CPF --> {mostra_cpf(cpf)} é VÁLIDO.')
    else:
        print(f'O CPF --> {mostra_cpf(cpf)} NÃO é válido')
    #informar o resultado

except:
    pass






cpf = '95120483020'
cpf = [int(x) for x in cpf]
cpf = cpf[0:9]
# print(len(cpf))
