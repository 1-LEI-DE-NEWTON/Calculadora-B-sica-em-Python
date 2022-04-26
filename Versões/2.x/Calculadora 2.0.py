class operacoes:
  def soma(x,y):
    return x+y
  def sub (x,y):
    return x-y
  def multp (x,y):
    return x*y
  def div (x,y):
    return x/y

def Denovo():
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
  sendo +,-,* ou /''' + '\n')
  
  basico = {
  '+': operacoes.soma,
  '-': operacoes.sub,
  '*': operacoes.multp,
  '/': operacoes.div    
  }
  
  if operador in basico:
   numero1= int(input ('informe o primeiro número ' + '\n'))
   numero2= int(input ('informe o segundo número ' + '\n'))
   print(numero1, operador, numero2, "=", basico[operador](numero1, numero2))
   Denovo()
  else: 
    operadorNaoValido()

calculadora()
