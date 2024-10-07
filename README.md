# Verificador de CPF em Python

Este repositório contém um script Python que verifica a validade de um CPF. O script foi criado com base nas regras de validação oficiais para CPFs brasileiros e utiliza apenas recursos nativos da linguagem Python.

O script inclui uma função que recebe uma string contendo um CPF e retorna True se o CPF é válido ou False caso contrário. Ele remove os pontos e o hífen (caso existam) e verifica se a string tem 11 caracteres numéricos. Em seguida, ele calcula os dígitos verificadores e verifica se eles são iguais aos dígitos do CPF fornecido.

Embora a implementação seja básica e não considere alguns casos específicos, como CPFs com números repetidos ou CPFs inválidos que podem ser gerados com a lógica de verificação, ela pode ser útil para fins educacionais ou como ponto de partida para uma implementação mais robusta.
