def verificar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")  # remove pontos e hífen
    if len(cpf) != 11 or not cpf.isdigit():
        return False  # CPF deve ter 11 dígitos numéricos

    # Verifica o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto
    if int(cpf[9]) != digito1:
        return False

    # Verifica o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto
    if int(cpf[10]) != digito2:
        return False

    return True  # CPF válido

cpf = input("Digite um CPF para verificar: ")
if verificar_cpf(cpf):
    print("CPF válido!")
else:
    print("CPF inválido!")


'''
O código acima define uma função verificar_cpf que recebe uma string contendo o CPF a ser verificado. Ele remove os pontos e o hífen (caso existam) e verifica se a string tem 11 caracteres numéricos. Em seguida, ele calcula os dígitos verificadores e verifica se eles são iguais aos dígitos do CPF fornecido. Se tudo estiver correto, a função retorna True, indicando que o CPF é válido. Caso contrário, retorna False.
'''

'''
Note que esse script é apenas uma implementação básica e não leva em conta alguns casos específicos, como CPFs com números repetidos ou CPFs inválidos que podem ser gerados com a lógica de verificação. Caso necessite de uma validação mais complexa, é recomendado a utilização de uma biblioteca externa específica para validação de CPF.
'''
