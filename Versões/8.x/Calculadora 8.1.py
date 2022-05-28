from math import log, factorial
import re
import time

class Operacoes:

  def soma(x,y):
    return x+y
  def sub (x,y):
    return x-y
  def multp (x,y):
    return x*y
  def div (x,y):
    return x/y
  def raizQ (x):
    return pow (x,0.5)
  def exp (x,y):
    return x**y
  def logXY(x,y):
    return log(x,y)
  def logX10(x):
    return log(x,10)
  def ln(x):
    return log(x)
  def logX2(x):
    return log(x,2)
  def fatorial(x):
    return factorial(x) 

basico = {
  '+': Operacoes.soma,
  '-': Operacoes.sub,
  '*': Operacoes.multp,
  '/': Operacoes.div,
  '**': Operacoes.exp    
  }
  
intermediário = {
  'r': Operacoes.raizQ,
  '!': Operacoes.fatorial
  }    

avançado = {
  'log': Operacoes.logXY,
  'log10': Operacoes.logX10,
  'ln': Operacoes.ln,
  'log2': Operacoes.logX2
}
  
def stringsrapidas():
  digitacao= 'Digite s, se sim e n, se não.'
  saindo='Até logo!'
  resultado='Resultado:'
  invalido= 'Você não escolheu uma opção válida. Por favor selecione uma opção válida.'
  somente= 'Digite apenas números!'
  CE_Fatorial= 'Só é possível calcular o fatorial de números naturais (números inteiros positivos)'
  CE_Raiz_Q= 'Só é possível calcular raiz quadrada de números reais'
  CE_Log_Real= 'Só é possível calcular logaritmos de números reais'
  regex_reais= '(?<![a-zA-Z:])[-+]?\d*\.?\d+$'
  regex_naturais= '[+]?\d+$'
  regex_inteiros_positivos= '[+]?\d*\.?\d+$'
  logd= 'o logaritmo de'
  ln= 'o logaritmo natural (base e) de'
  return digitacao,saindo,resultado, invalido, somente, regex_reais, logd, regex_naturais, CE_Fatorial, regex_inteiros_positivos, CE_Raiz_Q, CE_Log_Real, ln
digitacao, saindo, resultado, invalido, somente, regex_reais, logd, regex_naturais, CE_fatorial, regex_inteiros_positivos, CE_Raiz_Q, CE_Log_Real, ln = stringsrapidas()

class Testes:

  def teste1(numero1): 
    while re.fullmatch(f'{regex_reais}', numero1) is None: 
      print(f'{somente}')
      Menu.numeros_basicos1()
    return numero1  
  
  def teste2(numero2): 
    while re.fullmatch(f'{regex_reais}', numero2) is None: 
      print(f'{somente}')
      Menu.numeros_basicos2()
    return numero2

  def teste3(numero3): 
    while re.fullmatch(f'{regex_reais}', numero3) is None: 
      print(f'{somente}')
      Menu.matematica()
    while re.fullmatch(f'{regex_inteiros_positivos}', numero3) is None: 
      print(f'{CE_Raiz_Q}')
      Menu.matematica()
    return numero3   
  
  def teste4(numero4):
    while re.fullmatch(f'{regex_reais}', numero4) is None: 
      print(f'{somente}')
      Menu.matematica()
    while re.fullmatch(f'{regex_inteiros_positivos}', numero4) is None:
      print(f'{CE_Log_Real}')
      Menu.matematica()
    return numero4

  def teste5(numero5):
    while re.fullmatch(f'{regex_reais}', numero5) is None: 
      print(f'{somente}')
      Menu.matematica()
    return numero5

  def teste6 (numero6):
    while re.fullmatch(f'{regex_reais}', numero6) is None: 
      print(f'{somente}')
      Menu.matematica()
    while re.fullmatch(f'{regex_naturais}', numero6) is None:
      print(f'{CE_fatorial}')
      Menu.matematica()
    return numero6

class Menu:
  
  def bemvindo():
   print('Bem-vindo à Calculadora! Vamos brincar de matemática! 🤓')
   time.sleep(1.5)
   Menu.operadores()

  def operadores():
    global operador
    operador= input('''informe a operação matemática
  sendo: 
  + = soma
  - = subtração
  / = divisão
  * = multiplicação
  r = raiz quadrada
  ** = exponenciação
  log = logaritmo numa base qualquer
  log2 = logaritmo na base 2
  log10 = logaritmo na base 10
  ln = logaritmo natural
  ! = fatorial''' + '\n')
    Menu.matematica()

  def matematica():
    if operador in basico:
      Menu.numeros_basicos1()
    elif operador in intermediário:
      Menu.numeros_intermediários()
    elif operador in avançado:
      Menu.numeros_avançados1()
    else: 
      Iterações.operador_nao_valido()
            
  def numeros_basicos1():
    global numero1
    if operador =='**':
      numero1= (input ('informe a base' + '\n'))
      Testes.teste1(numero1)
      Menu.numeros_basicos2()
    else:
      numero1= (input ('informe o primeiro número' + '\n'))
      Testes.teste1(numero1)
      Menu.numeros_basicos2()

  def numeros_basicos2():
    if operador =='**':
      numero2= (input ('informe o expoente' + '\n'))
      Testes.teste2(numero2)
      print(f'{resultado}', float(numero1), 'elevado a', float(numero2), 'é:', basico[operador](float(numero1), float(numero2)))
      Iterações.denovo()
    else:
      numero2= (input ('informe o segundo número' + '\n'))
      Testes.teste2(numero2)
      print(f'{resultado}', float(numero1), operador, float(numero2), 'é:', basico[operador](float(numero1), float(numero2)))
      Iterações.denovo()
  
  def numeros_intermediários():
    if operador == 'r':
      numero3= (input ('informe o numero para cálculo da raíz quadrada' + '\n'))
      Testes.teste3(numero3)
      print('raiz de', float(numero3), 'é:', intermediário[operador](float(numero3)))
      Iterações.denovo()
    elif operador == '!':
      numero6= (input ('informe o numero para cálculo do fatorial' + '\n'))
      Testes.teste6(numero6)
      print('fatorial de', numero6, 'é:', intermediário[operador](int(numero6)))
      Iterações.denovo()

  
  def numeros_avançados1():
    global numero4
    numero4= (input ('informe o logaritmando' + '\n'))
    Testes.teste4(numero4)
    if operador == 'log':
      Menu.numeros_avançados2()
    elif operador == 'log10':
      print(f'{logd}', numero4, 'na base 10 é:', avançado[operador](float(numero4)))
      Iterações.denovo()
    elif operador == 'ln':
      print(f'{ln}', numero4, 'é:', avançado[operador](float(numero4)))
      Iterações.denovo()
    elif operador == 'log2':
      print(f'{logd}', numero4, 'na base 2 é:', avançado[operador](float(numero4)))
      Iterações.denovo()

  def numeros_avançados2():
    numero5= (input ('informe a base' + '\n'))
    Testes.teste5(numero5)
    print(f'{logd}', numero4, 'na base', numero5, 'é:', avançado[operador](float(numero4) ,float(numero5)))
    Iterações.denovo()

class Iterações:

  def denovo():
    time.sleep(0.5) 
    denovo= input (f'''Gostaria de continuar calculando?
{digitacao}''' + '\n')
    if denovo == 's':
      Menu.operadores()
    elif denovo == 'n':
      print(f'{saindo}')
      quit()
    else:
      print (f'{invalido}')
      Iterações.denovo()
   
  def operador_nao_valido():
    invalidez= input (f'''Operação inválida. Gostaria de tentar denovo?
{digitacao}''' + '\n')
    if invalidez == 's':
      Menu.operadores()
    elif invalidez == 'n':
      print(f'{saindo}')
      quit()
    else:
      print (f'{invalido}')
      Iterações.operador_nao_valido()  


Menu.bemvindo()
