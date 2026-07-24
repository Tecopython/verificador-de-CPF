def confere(cpf:list) -> bool:
    '''Recebe uma lista contendo os números do CPF e retorna um booleano indicando se o CPF é válido'''
    cpf_c = cpf[0:9]
    #levantando o primeiro dígito verificador
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
    
    #levantando o segundo dígito verificador
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
    #comparando o CPF original com o montado dentro da função
    if cpf == cpf_c:
        return True
    else:
        return False

def mostra_cpf(cpf:list) -> str:
    '''Recebe uma lista de números do CPF digitado e retorna uma string com o CPF formatado'''
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


def main():
    while True:
        try:
            #Solicitando o CPF ao usuário
            cpf = input('Digite o CPF (sem "." e e sem "-") --> ')
            #transformando a string em uma lista de inteiros
            cpf = [int(x) for x in cpf]
            #checando se o CPF tem 11 dígitos
            if len(cpf) > 11:
                print('\nVocê colocou números demais, revise\n')
                continue
            elif len(cpf) < 11:
                print('\nEstá faltando números, confira novamente\n')
                continue
            else:
                break
        except ValueError:
            print(f'\n\nVocê não digitou um número válido\n')
        except KeyboardInterrupt:
            print("\n\nUsuário desconectou pelo teclado\n")
            break

    #informando se o CPF é válido ou não
    try:
        if confere(cpf):
                print(f'O CPF --> {mostra_cpf(cpf)} é VÁLIDO.')
        else:
            print(f'O CPF --> {mostra_cpf(cpf)} NÃO é válido')
    except:
        pass

if __name__ == '__main__':
    main()