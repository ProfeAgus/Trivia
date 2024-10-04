"""
Juego de Trivia

El proposito es que puedan entregar un juego de trivia que tenga
- varias categorias 
- en donde puedan jugar de a 2 jugadores

formato de las preguntas
cada pregunta está en una lista donde el primer elemento es la pregunta, hay 4 opciones y el ultimo elemento es posicion en donde está la respuesta
vean los ejemplos en el codigo

para estar aprobado es necesario
1. que el juego corra
2. que se pueda jugar de a 2 personas
3. que las preguntas sean aleatorias
4. que se usen funciones para hacer el codigo mas leible y mas facil a la hora de programar
5. al finalizar el juego que muestre el puntaje de cada jugador y determine el ganador o un empate

para sumar puntos extra:
1. que no se repitan preguntas
2. creatividad

cosas que van a restar puntos:
1. repetir codigo, si se dan cuenta que estan programando lo mismo o algo parecido mas de una vez, es mejor hacer o usar una funcion

se les da algunas declaraciones de funciones, variables y listas que van a probablemente usar para programar el juego, para que las implementen en clase. algunas lo haran con 
el profe, otras las van a tener que pensar ustedes
"""

import random, os, time

if os.name == "nt":
    limpiar = "cls"
else:
    limpiar = "clear"

ingles = [
        ["Que significa dog ?", "1. perro", "2. gato", "3. tortuga", "4. casa", 1 ]
    ]

historia = [
    ["cual es el año de independencia argentina ?","1. 1810", "2. 1812", "3. 1816", "4. 1820",3]
    ]

ciencia = [
    ["De que color es el cielo en Perú ?","1. verde", "2. amarillo", "3. marron", "4. celeste",4 ]
    ]

preguntas = [ingles, historia, ciencia]
nombre_categoria = ["Inglés", "Historia", "Ciencia"]

preguntas_ya_preguntado = []

def limpiar_pantalla():
    os.system(limpiar)

def esperar(segundos: int):
    time.sleep(segundos)

def elegir_categoria()->int:
    """Devuelve la posicion de la categoria en la lista de preguntas"""
    pass

def elegir_pregunta( categoria: int)->int:
    """Devuelve la posicion de una pregunta, dependiendo de la categoria"""
    pass

def mostrar_pregunta(categoria: int, pregunta: int):
    """muestra en pantalla la pregunta con las opciones"""
    pass
    
def fue_elegida_antes(categoria: int, pregunta: int)->bool:
    """ True si ya fue preguntado """
    pass

def respuesta_correcta(categoria: int, pregunta: int, respuesta_jugador: int)->bool:
    """True si la respuesta del jugador es correcta"""
    pass

def juego():
    """Aca es donde se tiene la logica del juego"""
    pass    
    
                    
juego()