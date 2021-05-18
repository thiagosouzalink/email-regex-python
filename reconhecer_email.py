import re



# Regex para nome de usuário
nome_usuario_email = r"^([a-zA-Z]\w+)"

# Regex para domínio
dominio_email = r"(([a-z])+(\.[a-z]{2,3})(\.[a-z]{1,2})?)$"

# Convatenação para verficar Regex do email
email = f"{nome_usuario_email}@{dominio_email}"

# Compila o padão Regex
emailRegex = re.compile(email)

# Lista de E-mail para serem verficados
lista_emails = ['johntravolta@mail.com', 'bonovox@mail.com.br', 'ronaldofenomeno@mail', 'cristianoronaldo@mail.com.hgd', 
                'mail.com.br', 'osvaldocruz@mail.com', 'emailinvalidodasilva@']

# Laço para percorer a lista de e-mail
for email in lista_emails:
    # Faz busca do padrão de email
    verificador = emailRegex.search(email)
    # Imprime o resultado
    if verificador:
        print(f'E-mail válido: {verificador.group()}')
    else:
        print(f'E-mail inválido: {email}')

# E-mail válido: johntravolta@mail.com
# E-mail válido: bonovox@mail.com.br
# E-mail inválido: ronaldofenomeno@mail
# E-mail inválido: cristianoronaldo@mail.com.hgd
# E-mail inválido: mail.com.br
# E-mail válido: osvaldocruz@mail.com
# E-mail inválido: emailinvalidodasilva@