
from math import log, factorial, sin, cos, tan, asin, acos, atan, sinh, cosh, tanh, acosh, asinh, atanh, degrees, radians
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
  def seno(x):
    return sin(x)
  def cosseno(x):
    return cos(x)
  def tangente(x):
    return tan(x)
  def senh(x):
    return sinh(x)
  def cosh(x):
    return cosh(x)
  def tgh(x):
    return tanh(x)
  def arcseno(x):
    return asin(x)
  def arccos(x):
    return acos(x)
  def arctg(x):
    return atan(x)
  def arcsenh(x):
    return asinh(x)
  def arccosh(x):
    return acosh(x)
  def arctgh(x):
    return atanh(x)
  def rad_p_graus(x):
    return degrees(x)
  def graus_p_rad(x):
    return radians(x)

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

trigonometria = {
  'sen': Operacoes.seno,
  'cos': Operacoes.cosseno,
  'tg': Operacoes.tangente,
}

trigonometria_hiperbolica = {
  'senh': Operacoes.senh,
  'cosh': Operacoes.cosh,
  'tgh': Operacoes.tgh,
}

trigonometria_inversa = {
  'arcsen': Operacoes.arcseno,
  'arccos': Operacoes.arccos,
  'arctg': Operacoes.arctg,
}

trigonometria_hiperbolica_inversa = {
  'arcsenh': Operacoes.arcsenh,
  'arccosh': Operacoes.arccosh,
  'arctgh': Operacoes.arctgh,
}

conversões ={
  'radianos_graus': Operacoes.rad_p_graus,
  'graus_radianos': Operacoes.graus_p_rad
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
  operação_diferente = 'A operação escolhida não é válida para o número digitado.'
  return digitacao,saindo,resultado, invalido, somente, regex_reais, logd, regex_naturais, CE_Fatorial, regex_inteiros_positivos, CE_Raiz_Q, CE_Log_Real, ln, operação_diferente
digitacao, saindo, resultado, invalido, somente, regex_reais, logd, regex_naturais, CE_fatorial, regex_inteiros_positivos, CE_Raiz_Q, CE_Log_Real, ln, operação_diferente = stringsrapidas()

class Testes:

  def reais(x): 
    while re.fullmatch(f'{regex_reais}', x) is None: 
      print(f'{somente}')
      Menu.numeros_basicos1()
    return x
    
  def inteiros_positivos_raizq(x): 
    while re.fullmatch(f'{regex_reais}', x) is None: 
      print(f'{somente}')
      Menu.matematica()
    while re.fullmatch(f'{regex_inteiros_positivos}', x) is None: 
      print(f'{CE_Raiz_Q}')
      Menu.matematica()
    return x   
  
  def inteiros_positivos_log(x):
    while re.fullmatch(f'{regex_reais}', x) is None: 
      print(f'{somente}')
      Menu.matematica()
    while re.fullmatch(f'{regex_inteiros_positivos}', x) is None:
      print(f'{CE_Log_Real}')
      Menu.matematica()
    return x

  def naturais_fatorial(x):
    while re.fullmatch(f'{regex_reais}', x) is None: 
      print(f'{somente}')
      Menu.matematica()
    while re.fullmatch(f'{regex_naturais}', x) is None:
      print(f'{CE_fatorial}')
      Menu.matematica()
    return x

class Menu:
  
  def bemvindo():
   print('Bem-vindo à Calculadora! Vamos brincar de matemática! 🤓')
   time.sleep(1.5)
   Menu.operadores()

  def operadores():
    global operador
    print('''opções disponíveis:
      1 basicas: adição, subtração, multiplicação, divisão e exponenciação
      2 intermediarias: radiciação, fatorial
      3 avancadas: logaritmo de qualquer base e logaritmo natural (base e)
      4 trigonometria: seno, cosseno, tangente
      5 trigonometria hiperbólica: seno hiperbólico, cosseno hiperbólico, tangente hiperbólica
      6 conversoes: converter radianos para graus
      7 trigonometria inversa: arcseno, arccosseno, arctangente
      8 trigonometria hiperbólica inversa: arcseno hiperbólico, arccosseno hiperbólico, arctangente hiperbólica
        ''')
    tipos_operacoes = input('informe a opção desejada:' + '\n' )
    if tipos_operacoes == '1':
      operador = input('''informe a operação matemática
      sendo: 
      + = soma
      - = subtração
      / = divisão
      * = multiplicação
      ** = exponenciação
      ''')
      if operador not in basico:
        print(f'{operação_diferente}')
        Menu.operadores()

    elif tipos_operacoes == '2':
      operador = input('''informe a operação matemática
      sendo:
      r = radiciação
      ! = fatorial
      ''')
      if operador not in intermediário:
        print(f'{operação_diferente}')
        Menu.operadores()
    elif tipos_operacoes == '3':
      operador = input('''informe a operação matemática
      sendo:
      log = logaritmo natural
      log10 = logaritmo em base 10
      ln = logaritmo natural
      log2 = logaritmo em base 2
      ''')
      if operador not in avançado:
        print(f'{operação_diferente}')
        Menu.operadores()
    elif tipos_operacoes == '4':
      operador = input('''informe a operação matemática
      sendo:
      sen = seno
      cos = cosseno
      tg = tangente
      arcseno = arcoseno
      arccos = arcocosseno
      arctg = arcotangente
      ''')
      if operador not in trigonometria:
        print(f'{operação_diferente}')
        Menu.operadores()
    elif tipos_operacoes == '5':
      operador = input('''informe a operação matemática
      sendo:
      senh = seno hiperbólico
      cosh = cosseno hiperbólico
      tgh = tangente hiperbólica
      arcsenh = arcoseno hiperbólico
      arccosh = arcocosseno hiperbólico
      arctgh = arcotangente hiperbólica
      ''')
      if operador not in trigonometria_hiperbolica:
        print(f'{operação_diferente}')
        Menu.operadores()
    elif tipos_operacoes == '6':
        operador = input('''escolha a opção mais adequada:
        1 = converter radianos para graus
        2 = converter graus para radianos
        ''')
        if operador == '1':
          operador = 'radianos_graus'
        elif operador == '2':
          operador = 'graus_radianos'
        if operador not in conversões:
          print(f'{operação_diferente}')
          Menu.operadores()
    elif tipos_operacoes == '7':
        operador = input('''informe a operação matemática
      sendo:
      arcsen = arcoseno
      arccos = arcocosseno
      arctg = arcotangente
      ''')
        if operador not in trigonometria_inversa:
          print(f'{operação_diferente}')
          Menu.operadores()
    elif tipos_operacoes == '8':
        operador = input('''informe a operação matemática
      sendo:
      arcsenh = arcoseno hiperbólico
      arccosh = arcocosseno hiperbólico
      arctgh = arcotangente hiperbólico
      ''')
        if operador not in trigonometria_hiperbolica_inversa:
          print(f'{operação_diferente}')
          Menu.operadores()
    else:
      print('operação inválida')
      Menu.operadores()
    Menu.matematica()

  def matematica():
    if operador not in basico and operador not in intermediário and operador not in avançado and operador not in trigonometria and operador not in conversões and operador not in trigonometria_hiperbolica and operador not in trigonometria_inversa and operador not in trigonometria_hiperbolica_inversa:
      Iterações.operador_nao_valido()
    if operador in basico:
      Menu.numeros_basicos1()
    elif operador in intermediário:
      Menu.numeros_intermediários()
    elif operador in avançado:
      Menu.numeros_avançados1()
    elif operador in trigonometria:
      Menu.numeros_trigonometria()
    elif operador in trigonometria_hiperbolica:
      Menu.numeros_trigonometria_hiperbolica()
    elif operador in conversões:
      Menu.converter_angulos()
    elif operador in trigonometria_inversa:
      Menu.numeros_trigonometria_inversa()
    elif operador in trigonometria_hiperbolica_inversa:
      Menu.numeros_trigonometria_inversa_hiperbolica()

            
  def numeros_basicos1():
    global exp_base
    global numero1
    if not operador =='**':
      numero1= (input ('informe o primeiro número' + '\n'))
      Testes.reais(numero1)
      Menu.numeros_basicos2()
    if operador =='**':
      exp_base= (input ('informe a base' + '\n'))
      Testes.reais(exp_base)
      Menu.numeros_basicos2()

  def numeros_basicos2():
    if not operador =='**':
      numero2= (input ('informe o segundo número' + '\n'))
      Testes.reais(numero2)
      print(f'{resultado}', float(numero1), operador, float(numero2), 'é:', basico[operador](float(numero1), float(numero2)))
      Iterações.denovo()
    if operador =='**':
      exp_expoente= (input ('informe o expoente' + '\n'))
      Testes.reais(exp_expoente)
      print(f'{resultado}', float(exp_base), 'elevado a', float(exp_expoente), 'é:', basico[operador](float(exp_base), float(exp_expoente)))
      Iterações.denovo()
  
  def numeros_intermediários():
    if operador == 'r':
      raizq= (input ('informe o numero para cálculo da raíz quadrada' + '\n'))
      Testes.inteiros_positivos_raizq(raizq)
      print('raiz de', float(raizq), 'é:', intermediário[operador](float(raizq)))
      Iterações.denovo()
    elif operador == '!':
      fatorial= (input ('informe o numero para cálculo do fatorial' + '\n'))
      Testes.naturais_fatorial(fatorial)
      print('fatorial de', fatorial, 'é:', intermediário[operador](int(fatorial)))
      Iterações.denovo()

  
  def numeros_avançados1():
    global log_logaritmando
    log_logaritmando= (input ('informe o logaritmando' + '\n'))
    Testes.inteiros_positivos_log(log_logaritmando)
    if operador == 'log':
      Menu.numeros_avançados2()
    elif operador == 'log10':
      print(f'{logd}', log_logaritmando, 'na base 10 é:', avançado[operador](float(log_logaritmando)))
      Iterações.denovo()
    elif operador == 'ln':
      print(f'{ln}', log_logaritmando, 'é:', avançado[operador](float(log_logaritmando)))
      Iterações.denovo()
    elif operador == 'log2':
      print(f'{logd}', log_logaritmando, 'na base 2 é:', avançado[operador](float(log_logaritmando)))
      Iterações.denovo()

  def numeros_avançados2():
    log_base= (input ('informe a base' + '\n'))
    Testes.reais(log_base)
    print(f'{logd}', log_logaritmando, 'na base', log_base, 'é:', avançado[operador](float(log_logaritmando) ,float(log_base)))
    Iterações.denovo()
  
  def numeros_trigonometria():
    tipo_angulo = input('O angulo está em graus ou em radianos?' + '\n' )
    angulo = input('informe o angulo' + '\n' )
    Testes.reais(angulo)
    if tipo_angulo == 'graus':
      angulo = Operacoes.graus_p_rad(float(angulo))      
    if operador == 'sen':
        print('seno de', angulo, 'é:', trigonometria[operador](float(angulo)), 'graus')
        Iterações.denovo()
    elif operador == 'cos':
        print('cosseno de', angulo, 'é:', trigonometria[operador](float(angulo)), 'graus')
        Iterações.denovo()
    elif operador == 'tg':
        print('tangente de', angulo, 'é:', trigonometria[operador](float(angulo)), 'graus')
        Iterações.denovo()

  def numeros_trigonometria_hiperbolica():
    hiperbolico = input('informe o hiperbólico' + '\n' )
    Testes.reais(hiperbolico)
    if operador == 'senh':
        print('seno hiperbólico de', hiperbolico, 'é:', trigonometria_hiperbolica[operador](float(hiperbolico)))
        Iterações.denovo()
    elif operador == 'cosh':
        print('cosseno hiperbólico de', hiperbolico, 'é:', trigonometria_hiperbolica[operador](float(hiperbolico)))
        Iterações.denovo()
    elif operador == 'tgh':
        print('tangente hiperbólica de', hiperbolico, 'é:', trigonometria_hiperbolica[operador](float(hiperbolico)))
        Iterações.denovo()
  
  def numeros_trigonometria_inversa():
    inverso = input('informe o inverso para cálculo do ângulo, em graus' + '\n' )
    Testes.reais(inverso) 
    if operador == 'arcsen':
        print('arcsen de', inverso, 'é:', Operacoes.rad_p_graus(trigonometria_inversa[operador](float(inverso))))
        Iterações.denovo()
    elif operador == 'arccos':
        print('arccos de', inverso, 'é:', Operacoes.rad_p_graus(trigonometria_inversa[operador](float(inverso))))
        Iterações.denovo()
    elif operador == 'arctg':
        print('arctg de', inverso, 'é:', Operacoes.rad_p_graus(trigonometria_inversa[operador](float(inverso))))
        Iterações.denovo()

  def numeros_trigonometria_inversa_hiperbolica():
    hiperbolico_inverso = input('informe o hiperbólico inverso' + '\n' )
    Testes.reais(hiperbolico_inverso)
    if operador == 'arcsenh':
        print('arcsenh de', hiperbolico_inverso, 'é:', trigonometria_hiperbolica_inversa[operador](float(hiperbolico_inverso)))
        Iterações.denovo()
    elif operador == 'arccosh':
        print('arccosh de', hiperbolico_inverso, 'é:', trigonometria_hiperbolica_inversa[operador](float(hiperbolico_inverso)))
        Iterações.denovo()
    elif operador == 'arctgh':
        print('arctgh de', hiperbolico_inverso, 'é:', trigonometria_hiperbolica_inversa[operador](float(hiperbolico_inverso)))
        Iterações.denovo()
  
  def converter_angulos():
    angulo = input('informe o angulo a ser convertido' + '\n' )
    Testes.reais(angulo)
    if operador == 'radianos_graus':
        print(angulo,'radiano(s) é:', Operacoes.rad_p_graus(float(angulo)), 'graus')
        Iterações.denovo()
    elif operador == 'graus_radianos':
        print(angulo,'graus é:', Operacoes.graus_p_rad(float(angulo)), 'radiano(s)')
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
