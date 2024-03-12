#login de usuario por cpf e senha.

print('com o cadastro efetuado inicie o login')
cpf = input("digite seu cpf: ")
len (cpf) == 11 
senha = input("digite sua senha: ")
len (senha) >= 6
print("login efetuado com sucesso!")

# usuario cadastrar nova escola no sistema

email = input('insira seu email aluno')
print('cadastre nova escola!')
inf1 = input('digite o nome da escola que deseja: ')
inf2 = input('digite o endereco da escola: ')
inf3 = input ('digite o numero de telefone da escola: ')
inf4 = input('digite o email institucional: ')
print('escola cadastrada com sucesso!!!!')

# cadastro de professores em uma escola
escola = input('digite a escola que deseja cadastrar o professor: ')
prof = input('digite o nome do professor:  ')
end = input('digite o cep do professor: ')
len (end) == 8
print("professor cadastrado na escola com sucesso!! ")

#cadastro de alunos para os professores.
dig1 = input('digite a escola desejada: ')
dig2 = input('digite o nome do professor :')
#professor e escolas ja cadastradas no sistema...
aln = input('digite o nome do aluno:')
dig3 = input('digite o cep do aluno: ')
len (dig3) == 8
dig4 = input('digite o cpf do aluno:')
len (dig4) == 11
print ('aluno associado a professor e escola!')
print("VOCE FOI CADASTRADO COM SUCESSO!!!!")
