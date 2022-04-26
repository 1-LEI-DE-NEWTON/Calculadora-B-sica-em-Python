def calculadora():
  c= input ('informe a operação matemática ')
  x= int(input ('informe o primeiro número '))
  y= int(input ('informe o segundo número '))

  if c == "+":
    print (x, "+", y, "=", x+y)
  elif c == "-":
    print (x, "-", y, "=", x-y)
  elif c == "*":
    print (x, "*", y, "=", x*y)
  elif c == "/":
    print (x, "/",y, "=", x/y)
  else:
    d= input ("""
    operação inválida. Gostaria de tentar novamente?
    Digite s, se sim e n, se não.""")
    if d == "s":
      calculadora()
    if d == "n":
      print ("Adios")
    

calculadora()
