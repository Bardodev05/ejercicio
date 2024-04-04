#promedio de duracion 
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
curso_youtube = 1.5

#diferencias de duracion 
direrencia_cursos = 100 - curso_youtube / otros_cursos_min * 100
direrencia_cursos_max = 100 - curso_youtube * 1000 // otros_cursos_max / 10
direrencia_cursos_promedio = 100 - curso_youtube / otros_cursos_promedio * 100
print("---------------------------------")
print(f"el curso de youtube dura un {direrencia_cursos}& menos que el mas rapido")
print(f"el curso de youtube dura un {direrencia_cursos_max}& menos que el mas lento")
print(f"el curso de youtube dura un {direrencia_cursos_promedio}& menos que el promedio")
print("---------------------------------")

#diferencia de crudos 
crudo_promedio = 5
crudo_youtube = 3.5

#calculando porcentaje de tiempo vacio removido
tiempo_vacio_promedio = 100 - otros_cursos_promedio / crudo_promedio * 100
tiempo_vacio_youtube = 100 - curso_youtube *1000 // crudo_youtube / 10

#mostrando la cantida de tiempo que se remueve 
print(f"un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio")
print(f"este curso elmino el {tiempo_vacio_youtube}% de tiempo vacio")
print("---------------------------------")


#mostar diferencia si el curso durara 10 horas
print(f"ver 10 horas de este curso equivale a ver {otros_cursos_promedio *100 // curso_youtube / 10} horas de otros cursos")
print(f"ver 10 horas de este  otros curso equivale a ver {curso_youtube *100 // otros_cursos_promedio / 10} horas de otros cursos")
print("---------------------------------")