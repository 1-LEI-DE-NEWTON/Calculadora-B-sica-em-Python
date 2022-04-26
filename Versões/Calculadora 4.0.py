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

digitacao= 'Digite s, se sim e n, se não.'
saindo='Adios'
resultado='Resultado:'

def bemvindo():
  print('Bem-vindo à Calculadora! Vamos brincar de matemática 🤓')
  time.sleep(1.5)

def calculadora():
  
  operador= input('''informe a operação matemática
  sendo: 
  + = soma
  - = subtração
  / = divisão
  * = multiplicação
  r = raiz quadrada
  ** = exponenciação''' + '\n')
  
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

  if operador in basico:
   numero1= (input ('informe o primeiro número ' + '\n'))
   while not numero1.isdigit(): 
    print('Digite apenas números!')
    numero1= (input ('informe o primeiro número ' + '\n'))
    if numero1.isdigit():
     break
   numero2= (input ('informe o segundo número ' + '\n'))
   while not numero2.isdigit(): 
    print('Digite apenas números!')
    numero2= (input ('informe o primeiro número ' + '\n'))
    if numero2.isdigit():
     break
   print(f'{resultado}', float(numero1), operador, float(numero2), "=", basico[operador](float(numero1), float(numero2)))
   time.sleep(0.5)
   novamente()
  elif operador in intermediário:
   numero1= float(input ('informe o numero para cálculo da raíz quadrada' + '\n' ))
   print('raiz de', numero1, '=', intermediário[operador](numero1))
   time.sleep(0.5)
   novamente()
  else: 
    operadorNaoValido()

def novamente():
  denovo= input (f'''Gostaria de continuar calculando?
{digitacao}''' + '\n')
  
  if denovo == 's':
    calculadora()

  if denovo == 'n':
    print(f'{saindo}')

def operadorNaoValido():
  invalidez= input (f'''Operação inválida. Gostaria de tentar novamente?
{digitacao}''' + '\n')

  if invalidez == 's':
   calculadora()
  if invalidez == 'n':
   print(f'{saindo}')
  


bemvindo()
calculadora()
