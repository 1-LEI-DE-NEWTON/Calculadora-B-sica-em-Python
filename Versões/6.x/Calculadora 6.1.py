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
  invalido= 'Você não escolheu uma opção válida. Por favor selecione uma opção válida.'
  somente= 'Digite apenas números!'
  regex= '(?<![a-zA-Z:])[-+]?\d*\.?\d+'
  return digitacao,saindo,resultado, invalido, somente, regex
digitacao, saindo, resultado, invalido, somente, regex = stringsrapidas()

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
  ** = exponenciação''' + '\n')
    Menu.matematica()

  def matematica():
      if operador in basico:
        Menu.numeros_basicos1()
      elif operador in intermediário:
       Menu.numeros_intermediários()
      else: 
        Iterações.operador_nao_valido()
            
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

  def numeros_basicos1():
    global numero1
    numero1= (input ('informe o primeiro número' + '\n'))
    Menu.teste1(numero1)
    Menu.numeros_basicos2() 

  def numeros_basicos2():
    numero2= (input ('informe o segundo número' + '\n'))
    Menu.teste2(numero2)
    print(f'{resultado}', float(numero1), operador, float(numero2), "=", basico[operador](float(numero1), float(numero2)))
    time.sleep(0.5)
    Iterações.denovo()
  
  def numeros_intermediários():
    numero3= (input ('informe o numero para cálculo da raíz quadrada' + '\n' ))
    Menu.teste3(numero3)
    print('raiz de', float(numero3), '=', intermediário[operador](float(numero3)))
    time.sleep(0.5)
    Iterações.denovo()

class Iterações:

    def denovo():
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
