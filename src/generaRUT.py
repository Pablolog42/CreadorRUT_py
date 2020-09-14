import random



def generaDigitosRut():

    digitosRut = [random.randint(0,9) for i in range(7)]  # Crea Array con numeros aleatorios 
         
    digitosRut[0] = random.randint(0,2)     # Solo puedo partir con 0, 1 o 2
                                                          
    if digitosRut[0] == 2:                  
        digito2 = random.randint(1,3)       # Si el rut parte con 20 millones, que el segundo digito sea menor a 4
        digitosRut.insert(1, digito2)       # Se anexa en posición 2
    else:
        digito2 = random.randint(1,9)       # Si parte con 10 o 0 millones, que sea cualquiera distinto de 0
        digitosRut.insert(1, digito2)     
  
    return digitosRut



#def generaVerificador:
