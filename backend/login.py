from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import  Asistencia, User, Asignatura
from rest_framework import viewsets, permissions


@api_view(['POST'])
def login(request):
    data = JSONParser().parse(request)

    email = data['email']
    password = data['password']

    try:
        user = User.objects.get(email=email)
    except:
        return Response('Usuario Invalido')

    pass_valido = check_password(password, user.password)

    if not pass_valido:
        return Response('Password incorrecta')

    token, created = Token.objects.get_or_create(user=user)
    if user.tipo == "P":
        id_name = "idProfesor"
        rol = "Profesor"
    else:
        id_name = "idAlumno"
        rol = "Alumno"

    return Response({"token": token.key,
                    id_name: user.id,
                     "nombre": user.first_name,
                     "apellido": user.last_name,
                     "tipo": user.tipo,
                     "rol": rol,
                     "foto": user.foto,
                     "telefono": user.telefono,
                     "carreera": user.carrera,
                     "perfil": user.perfil,
                     })
