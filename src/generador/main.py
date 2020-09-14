from generaRUT import *

def main():

    n = int(input("Indique número de RUTs a generar: "))

    for x in range(n):
        
        rut = generaDigitosRut()

        verificador = str(generaVerificador(rut))  
        
        if verificador == "11": #Si el verif es 11, reemplazarlo por 0
            verificador = "0"
        
        if verificador == "10": #Si el verif es 10, reemplazarlo por k
            verificador = "k"

        rutString = "".join(map(str, rut))  #Pasar el array del rut sin verificador a un string

        rutCompleto = rutString + "-" + verificador

        print(rutCompleto) 

main()