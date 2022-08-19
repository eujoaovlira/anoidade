nome= (input('Nome Completo'));

inicio = True;

while inicio == True : 
  nascimento = int(input('Data de nascimento'));
  try:

    if (nascimento >= 1922 and  nascimento <= 2022):
      idade = 2022 - nascimento; 
      inicio = False ;
      print('Oi' + nome),
      print(idade)

    else:
      raise Exception


  except :
    print('Erro')  