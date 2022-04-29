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

basico = {
  '+': Operacoes.soma,
  '-': Operacoes.sub,
  '*': Operacoes.multp,
  '/': Operacoes.div,
  '**': Operacoes.exp    
  }
  
intermediário = {
  'r': Operacoes.raizQ
  }    

def stringsrapidas():
    digitacao= 'Digite s, se sim e n, se não.'
    saindo='Adios'
    resultado='Resultado:'
    return digitacao,saindo,resultado

digitacao, saindo, resultado = stringsrapidas()

class Menu:

  def bemvindo():
   print('Bem-vindo à Calculadora! Vamos brincar de matemática! 🤓')
   time.sleep(1.5)

  def operadores():
    operador= input('''informe a operação matemática
  sendo: 
  + = soma
  - = subtração
  / = divisão
  * = multiplicação
  r = raiz quadrada
  ** = exponenciação''' + '\n')
    Menu.matematica(operador)
    

  def matematica(operador):
      if operador in basico:
        numero1, numero2 = Menu.numeros_basico()
        print(f'{resultado}', float(numero1), operador, float(numero2), "=", basico[operador](float(numero1), float(numero2)))
        time.sleep(0.5)
        Menu.denovo()
      elif operador in intermediário:
        numero3 = Menu.numeros_intermediários()
        print('raiz de', float(numero3), '=', intermediário[operador](float(numero3)))
        time.sleep(0.5)
        Menu.denovo()
      else: 
        Menu.operadorNaoValido()

  def denovo():
   denovo= input (f'''Gostaria de continuar calculando?
{digitacao}''' + '\n')
  
   if denovo == 's':
    Menu.operadores()

   if denovo == 'n':
    print(f'{saindo}')
    exit()

  def operadorNaoValido():
   invalidez= input (f'''Operação inválida. Gostaria de tentar denovo?
{digitacao}''' + '\n')

   if invalidez == 's':
    Menu.operadores()
  
   if invalidez == 'n':
    print(f'{saindo}')
    exit()
     
  def teste1(numero1): 
     while re.fullmatch('(?<![a-zA-Z:])[-+]?\d*\.?\d+', numero1) is None: 
       print('Digite apenas números')
       Menu.matematica()
     return numero1  
  
  def teste2(numero2): 
     while re.fullmatch('(?<![a-zA-Z:])[-+]?\d*\.?\d+', numero2) is None: 
       print('Digite apenas números')
       Menu.matematica()
     return numero2

  def teste3(numero3): 
     while re.fullmatch('(?<![a-zA-Z:])[-+]?\d*\.?\d+', numero3) is None: 
       print('Digite apenas números')
       Menu.matematica()
     return numero3   

  def numeros_basico():
    numero1= (input ('informe o primeiro número' + '\n'))
    Menu.teste1(numero1)
    numero2= (input ('informe o segundo número' + '\n'))
    Menu.teste2(numero2)
    return numero1,numero2 

  def numeros_intermediários():
    numero3= (input ('informe o numero para cálculo da raíz quadrada' + '\n' ))
    Menu.teste3(numero3)
    return numero3  

Menu.bemvindo()
Menu.operadores()
