#2.  Faça um script que recebe um inteiro n e mostra todos os primos, de 1 até n. 

numero = int(input('Digite um valor: '))

if numero/1==numero and numero/numero==1 and numero%2 != 0:
    contador = 1
    while contador < numero:        
        if contador/1==contador and contador/contador==1:
            print(contador)
            contador +=1
        contador += 1
    print(numero)
  
   
else:
    print('não é primo')