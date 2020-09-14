from generaRUT import *

def main():

    n = int(input("Indique número de RUTs a generar: "))

    for x in range(n):
        rut = generaDigitosRut()
        verificador = str(generaVerificador(rut))

        rutString = "".join(map(str, rut)) 
  
        print(rutString + "-" + verificador) 

main()