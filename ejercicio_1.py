#promedio de duracion 
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
curso_youtube = 1.5

#diferencias de duracion 
direrencia_cursos = 100 - curso_youtube / otros_cursos_min * 100
direrencia_cursos_max = 100 - curso_youtube * 1000 // otros_cursos_max / 10
direrencia_cursos_promedio = 100 - curso_youtube / otros_cursos_promedio * 100

print(f"el curso de youtube dura un {direrencia_cursos}& menos que el mas rapido")
print(f"el curso de youtube dura un {direrencia_cursos_max}& menos que el mas lento")
print(f"el curso de youtube dura un {direrencia_cursos_promedio}& menos que el promedio")