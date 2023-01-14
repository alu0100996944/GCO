'''
# Alumno: Jefry Izquierdo Herández
# Asignatura: Gestion del Conocimiento en las Organizaciones.
# Practica: Sistema de recomendacion
# Objetivo: Implementar un sistema de recomendacion. 
# Ejecucxion del programa: python3 sistema-recomendacion.py matriz-[num]-[num]-[num].txt
'''

# Importar librerias
import sys 
import math
import numpy as np

# Comprobar numero de argumentos
nvar=1
if len(sys.argv) != nvar+1:
        sys.exit('El numero de argumentos no es el correcto ('+str(nvar)+')')
p=[(i) for i in sys.argv[1:nvar+1]]


####################

# Limpiar espacios en blanco
def LimpiarEspacios(usux, usuy):
    for i in range(len(usux)):
        if i < len(usux):
            newusux = usux[i].strip()
            newusuy = usuy[i].strip()
    return newusux, newusuy
 


####################

# Tratamiento de argumentos
# Leer linea a linea, guardando valoracion usuario
def LeerFichero():
    print ("+++ Matriz relacion usux/usuy de los usuarios ++++")
    datosusuario = []
    usux = []
    usuy = []
    with open("matriz.txt") as fname:
        usuarios = fname.readlines()
    for i in range(len(usuarios)):
        if i+1 < len(usuarios):
            usux.append(usuarios[i])
            usuy.append(usuarios[i+1])
            # Se llama al metodo para limpiar blancos y espacios
            newusux, newusuy = LimpiarEspacios(usux, usuy)
            print(newusux, newusuy)
            CoeficientePearson(newusux, newusuy)
      
    datosusuario.append(usuarios)
    print("\n")
    print("Matriz original de utilidad: ", datosusuario)
    print("usux: ", usux)
    print("usuy: ", usuy)
    return usux, usuy

print("\n") 


####################

# Calificaciones del usuario sobre el objeto
def CalificacionObjeto(usuario):
    resultado = []
    for i in range(len(usuario)):
        if i != "-" and i != " ":
            resultado.append(usuario[i])
    return resultado


####################

# Misma calificaciones de los dos usuarios sobre un objeto
def CalificacionIgualObjeto(usuariox, usuarioy):
    resultado = []
    for i in range(len(usuariox)):
        for j in range(len(usuarioy)):
            if i != "-" and i != " ":
                if usuariox[i] == usuarioy[j]:
                    resultado.append(usuariox[i])
    return resultado

####################

# Media
def Media(usux,usuy):
    sumax = 0
    sumay = 0
    lenvector = 0
    for i in range(len(usux)):
        for j in range(len(usuy)):
            if i < len(usux) and j < len(usuy):
                aux=int(i)
                aux2=int(j)
                sumax += aux
                sumay += aux2
                lenvector = lenvector+1
            if lenvector==0  or i =="-" or j =="-" or i ==" " or j ==" ":
                return 0,0
            else:
                xresult = float(sumax)/lenvector
                yresult = float(sumay)/lenvector
                i+1,j+1
    return xresult, yresult


####################

def CoeficientePearson(usuariox, usuarioy):
    pearson = []
    # Calificaciones del usuario sobre objeto i
    vcalificacionx = CalificacionObjeto(usuariox)
    vcalificaciony = CalificacionObjeto(usuarioy)
    
    # Media de calificaciones de los usuarios
    mediax, mediay = Media(vcalificacionx,vcalificaciony)
    

    numerador = 0.0
    xpow = 0.0
    ypow = 0.0
    for i in range(len(usuariox)):
        numerador += i-mediax*i-mediay
    for i in range(len(usuariox)):
        xpow += math.pow(i-mediax,2)
    for i in range(len(usuariox)):
        ypow += math.pow(i-mediay,2)
    # Producto de las raices cuadradas de los usuarios x e y    
    denominador = math.sqrt(xpow*ypow)
    pearson = numerador/denominador
    return pearson


####################

def DCoseno(usuariox, usuarioy):
    coseno = []
    # Calificaciones del usuario sobre objeto i
    vcalificacionx = CalificacionObjeto(usuariox)
    vcalificaciony = CalificacionObjeto(usuarioy)
    
    numerador = 0.0
    xpow = 0.0
    ypow = 0.0
    for i in range(len(vcalificacionx)):
        for j in range(len(vcalificaciony)):
            numerador = i*j
            xpow += math.pow(i,2)
            ypow += math.pow(j,2)
            denominador = math.sqrt(xpow*ypow)
    coseno = numerador/denominador
    return coseno

####################

def DEuclidea(usuariox, usuarioy):
    deuclidea = []
    # Calificaciones del usuario sobre objeto i
    vcalificacionx = CalificacionObjeto(usuariox)
    vcalificaciony = CalificacionObjeto(usuarioy)
    
    # Misma calificaciones de ambos usuarios sobre un objeto i
    vcalificacionxy = CalificacionIgualObjeto(vcalificacionx, vcalificaciony)
    
    xypow = 0.0
    for i in range(len(vcalificacionx)):
        for j in range(len(vcalificaciony)):
            xypow = math.pow(i-j,2)
    deuclidea = math.sqrt(xypow)
    return deuclidea

####################

def PrediccionSimple(similitud, vecinos, usuy):
    prediccion = []
    numerador = 0.0
    denominador = 0.0
    for i in range(len(usuy)):
        if i < vecinos: #Nku conjunto de los k vecinos, a medias
            numerador = similitud*i
        denominador = abs(similitud)
    prediccion = numerador/denominador
    return prediccion
        

####################

def PrediccionDMedia(similitud, vecinos, usux, usuy):
    prediccion = []
    mediax, mediay = Media(usux,usuy)
    numerador = 0.0
    denominador = 0.0
    for i in range(len(usuy)):
        if i < vecinos: #Nku conjunto de los k vecinos, a medias
            numerador = similitud*(i-mediay)
        denominador = abs(similitud)
    prediccion = numerador/denominador
    prediccion = prediccion + mediax
    return prediccion
    
    
####################

def SimilitudPearson(valor):
    if valor == 1:
        print("Correlacion directa perfecta")
    elif 0 < valor < 1:
        print("Correlacion directa")
    elif valor == 0:
        print("No hay correlacion")
    elif -0 < valor < 0:
        print("Correlacion inversa")
    elif valor == -1:
        print("Correlacion inversa perfecta")
    else:
        print("No se encuentra similitud")
        

####################

def SimilitudCoseno(valor):
    if valor == 1:
        print("Correlacion directa perfecta")
    elif 0 < valor < 1:
        print("Correlacion directa")
    elif valor == 0:
        print("No hay correlacion")
    else:
        print("No se encuentra similitud")
   
####################  
    
# Pedir numero, control de errores al recibir
def pedirNumeroEntero():
    correcto = False
    num = 0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
    return num
salir = False
opcion = 0

####################

# Menu para elegir las opciones
while not salir:
    print("OPCIONES DISPONIBLES")
    print ("1. Correlacion de Pearson")
    print ("2. Distancia coseno")
    print ("3. Distancia Euclidea")
    print ("4. Salir")
    
    print ("Elige una opcion")
    opcion = pedirNumeroEntero()
    print("####################################")
    if opcion == 1:
        print ("\nOpcion 1: 'Correlacion de Pearson'\n")
        
        # Matriz usuarios/recomendacion
        matriz = sys.argv[1]
        usux, usuy = LeerFichero()
        resultadopearson = CoeficientePearson(usux, usuy)
        print("\n")
        print("Coeficiente de Pearson: ", resultadopearson)
        print("\n")
        print("Similitud: ", SimilitudPearson(resultadopearson))
        print("\n")
        
    elif opcion == 2:
        print ("\nOpcion 2: 'Distancia coseno'\n")
        
        # Matriz usuarios/recomendacion
        matriz = sys.argv[1]
        usux, usuy = LeerFichero()
        resultadocoseno = DCoseno(usux, usuy)
        print("\n")
        print("Distancia Coseno: ", resultadocoseno)
        print("\n")
        print("Similitud: ", SimilitudCoseno(resultadocoseno))
        print("\n")
        
    elif opcion == 3:
        print("\nOpcion 3: 'Distancia Euclidea'\n")
        
        # Matriz usuarios/recomendacion
        matriz = sys.argv[1]
        usux, usuy = LeerFichero()
        resultadoeuclidea = DEuclidea(usux, usuy)
        print("\n")
        print("Distancia Euclidea: ", resultadoeuclidea)
        print("\n")
        
    elif opcion == 4:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")
        print("####################################")
        
    while True: 
        print("INTRODUCE EL NUMERO DE VECINOS CONSIDERADOS")
        vecinos = pedirNumeroEntero()
        if vecinos >= 3:
            break
        print("Introduce mas de 2 vecinos, minimo 3\n")
        
    
    while True:
        print("INTRODUCE EL TIPO DE PREDICCION")
        print ("1. Prediccion simple")
        print ("2. Diferencia con la media")
        prediccion = pedirNumeroEntero()
        if prediccion == 1:
            print ("\nOpcion 1: 'Prediccion simple'\n")
            if opcion == 1: #Correlacion de Pearson
                simipearson = CoeficientePearson(usux, usuy)
                prediccionspearson = PrediccionSimple(simipearson, vecinos, usuy)
                print("\n")
                print("Prediccion: ", prediccionspearson)
            elif opcion == 2: #Distancia Coseno
                simicoseno = DCoseno(usux, usuy)
                prediccionscoseno = PrediccionSimple(simicoseno, vecinos, usuy)
                print("\n")
                print("Prediccion: ", prediccionscoseno)
            elif opcion == 3: #Distancia Euclidea
                simieuclidea = DEuclidea(usux, usuy)
                prediccionseuclidea = PrediccionSimple(simieuclidea, vecinos, usuy)
                print("\n")
                print("Prediccion: ", prediccionseuclidea)
            else:
                print("Error con la prediccion simple")
        elif prediccion == 2:
            print ("\nOpcion 2: 'Diferencia con la media'\n")
            if opcion == 1: #Correlacion de Pearson
                simipearson = CoeficientePearson(usux, usuy)
                predicciondpearson = PrediccionDMedia(simipearson, vecinos, usux, usuy)
                print("\n")
                print("Prediccion: ", predicciondpearson)
            elif opcion == 2: #Distancia Coseno
                simicoseno = DCoseno(usux, usuy)
                predicciondcoseno = PrediccionDMedia(simicoseno, vecinos, usux, usuy)
                print("\n")
                print("Prediccion: ", predicciondcoseno)
            elif opcion == 3: #Distancia Euclidea
                simieuclidea = DEuclidea(usux, usuy)
                predicciondeuclidea = PrediccionDMedia(simieuclidea, vecinos, usux, usuy)
                print("\n")
                print("Prediccion: ", predicciondeuclidea)
            else:
                print("Error con la prediccion diferencia con la media")
        else:
            print("####################################")
            print ("Introduce un numero, 1 o 2")
            print("####################################")
print ("Fin")