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
  

def novamente():
  denovo= input ('''Mais alguma coisa?
  Digite s, se quiser continuar calculando e n, se nao''' + '\n')
  
  if denovo == 's':
    calculadora()

  if denovo == 'n':
    print('Adios')

def operadorNaoValido():
  invalidez= input ('''operação inválida. Gostaria de tentar novamente?
  Digite s, se sim e n, se não.''' + '\n')

  if invalidez == 's':
   calculadora()
  if invalidez == 'n':
   print('Adios')

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
   numero1= float(input ('informe o primeiro número ' + '\n'))
   numero2= float(input ('informe o segundo número ' + '\n'))
   print(numero1, operador, numero2, "=", basico[operador](numero1, numero2))
   novamente()
  elif operador in intermediário:
   numero1= float(input ('informe o numero para cálculo da raíz quadrada' + '\n' ))
   print('raiz de', numero1, '=', intermediário[operador](numero1))
   novamente()
  else: 
    operadorNaoValido()

calculadora()
