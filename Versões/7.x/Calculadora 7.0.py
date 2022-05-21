from math import log
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

basico = {
  '+': Operacoes.soma,
  '-': Operacoes.sub,
  '*': Operacoes.multp,
  '/': Operacoes.div,
  '**': Operacoes.exp    
  }
  
intermediário = {
  'r': Operacoes.raizQ,
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
  regex= '(?<![a-zA-Z:])[-+]?\d*\.?\d+'
  logd= 'o logaritmo de'
  return digitacao,saindo,resultado, invalido, somente, regex, logd
digitacao, saindo, resultado, invalido, somente, regex, logd = stringsrapidas()

class Testes:

  def teste1(numero1): 
    while re.fullmatch(f'{regex}', numero1) is None: 
      print(f'{somente}')
      Menu.numeros_basicos1()
    return numero1  
  
  def teste2(numero2): 
    while re.fullmatch(f'{regex}', numero2) is None: 
      print(f'{somente}')
      Menu.numeros_basicos2()
    return numero2

  def teste3(numero3): 
    while re.fullmatch(f'{regex}', numero3) is None: 
      print(f'{somente}')
      Menu.matematica()
    return numero3   
  
  def teste4(numero4):
    while re.fullmatch(f'{regex}', numero4) is None: 
      print(f'{somente}')
      Menu.matematica()
    return numero4

  def teste5(numero5):
    while re.fullmatch(f'{regex}', numero5) is None: 
      print(f'{somente}')
      Menu.matematica()
    return numero5

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
  ln = logaritmo natural''' + '\n')
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
    numero1= (input ('informe o primeiro número' + '\n'))
    Testes.teste1(numero1)
    Menu.numeros_basicos2()

  def numeros_basicos2():
    numero2= (input ('informe o segundo número' + '\n'))
    Testes.teste2(numero2)
    print(f'{resultado}', float(numero1), operador, float(numero2), "=", basico[operador](float(numero1), float(numero2)))
    Iterações.denovo()
  
  def numeros_intermediários():
    numero3= (input ('informe o numero para cálculo da raíz quadrada' + '\n' ))
    Testes.teste3(numero3)
    print('raiz de', float(numero3), '=', intermediário[operador](float(numero3)))
    Iterações.denovo()
  
  def numeros_avançados1():
    global numero4
    numero4= (input ('informe o logaritmando' + '\n'))
    Testes.teste4(numero4)
    if operador == 'log':
      Menu.numeros_avançados2()
    elif operador == 'log10':
      print(f'{logd}', numero4, 'na base 10 é', avançado[operador](float(numero4)))
      Iterações.denovo()
    elif operador == 'ln':
      print(f'{logd}', numero4, 'na base e é', avançado[operador](float(numero4)))
      Iterações.denovo()
    elif operador == 'log2':
      print(f'{logd}', numero4, 'na base 2 é', avançado[operador](float(numero4)))
      Iterações.denovo()

  def numeros_avançados2():
    numero5= (input ('informe a base' + '\n'))
    Testes.teste5(numero5)
    print(f'{logd}', numero4, 'na base', numero5, 'é', avançado[operador](float(numero4) ,float(numero5)))
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
