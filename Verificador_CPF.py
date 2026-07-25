class CPF:
    '''Classe que representa um CPF e contém métodos para validar e formatar o CPF, deve receber o CPF como uma string de 11 dígitos sem pontos e sem traço'''
    
    def __init__(self, cpf:str):
        self.cpf = cpf

    def __str__(self) -> str:
        return f'{self.formata_cpf()}'

    def tranforma_lista(self) -> list:
        '''Transforma o CPF em uma lista de números inteiros'''
        return [int(x) for x in self.cpf]
        

    def confere(self) -> bool:
        '''Confere se o CPF digitado é válido ou não'''
        if len(self.cpf) != 11:
            return False
        if self.cpf == self.cpf[0]*11:
            return False
        cpf_c = self.tranforma_lista()[:9]
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
        #comparando o CPF original com o montado dentro da função
        if self.tranforma_lista() == cpf_c:
            return True
        else:
            return False

    def formata_cpf(self) -> str:
        '''Recebe uma lista de números do CPF digitado e retorna uma string com o CPF formatado'''
        concat = ''
        contador = 1
        for x in self.cpf:
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

"Teste de verificação de CPF"
if __name__ == '__main__':
    while True:
        print("Você está em loop infinito de verificação de CPF, para sair pressione Ctrl + C")
        try:
            #Solicitando o CPF ao usuário
            cpf = input('Digite o CPF (sem "." e e sem "-") --> ')
            #verificando se o CPF digitado é um número e se tem 11 dígitos
            if not cpf.isdigit():
                print('\nVocê não digitou um número válido\n')
                continue
            if len(cpf) > 11:
                print('\nVocê colocou números demais, revise\n')
                continue
            elif len(cpf) < 11:
                print('\nEstá faltando números, confira novamente\n')
                continue
            else:
                cpf = CPF(cpf)
                if cpf.confere():
                    print(f'\n{cpf.formata_cpf()} --> VÁLIDO\n')    
                else:
                    print(f'\n{cpf.formata_cpf()} --> INVÁLIDO\n')       
        except KeyboardInterrupt:
            print("\n\nAté mais! \n")
            break
        except:
            break
