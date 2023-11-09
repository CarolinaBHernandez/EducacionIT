from django.db import models

MATERIAS = (
    ("Programación lógica", "Programación lógica"),
    ("Licenciatura en informática", (
        ("Algebra", "Algebra"),
        ("Programación Orientada a Objetos", "Programación Orientada a Objetos"),
    )),
    ("Licenciatura en economía", (
        ("Administración I", "Administración I"),
        ("Contabilidad", "Contabilidad"),
        ("Principios de economía", "Principios de economía"),
    )),
    ("Abogacía", (
        ("Introducción al derecho", "Introducción al derecho"),
        ("Teoría de la Persona", "Teoría de la Persona"),
        ("Derecho Penal I", "Derecho Penal I"),
    )),
)


class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    materia = models.CharField(max_length=100, choices=MATERIAS)

    def __str__(self):
        return self.nombre

