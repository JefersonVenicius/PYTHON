entrada = input('[E] para entrar e [S] para passar: ')
senha_digitada = input('Digite a senha de acesso: ')
senha = "123456789"

if (entrada == 'E' or entrada == 'e'):
    if (senha == senha_digitada):
        print("Sucesso, você entrou")
    else:
     print("Você não Entrou, Senha incorreta")
elif (entrada == 'S' or entrada == 's'):
   if (senha == senha_digitada):
    print("Sucesso, você passou")
   else:
    print("Você não Passou, senha incorreta")
else:
  print("Você não selecionou uma opção valida!")