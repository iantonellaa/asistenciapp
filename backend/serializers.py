from rest_framework import serializers
from .models import User,Asignatura,Asistencia


class User_Serializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ( 'email', 'password', 'first_name',
                  'last_name', 'tipo','foto',
                  'telefono','carrera','perfil')
        

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            tipo=validated_data['tipo'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    def update(self, instance, validated_data):
        update_user = super().update(instance, validated_data)
        update_user.set_password(validated_data['password'])
        update_user.save()
        return update_user

    def to_representation(self,instance):
        if instance.tipo == "P":
            tipo = "Profesor"
        else:
            tipo= "Alumno"
    
        return{
            'id' : instance.id,
            'email': instance.email,
            'first_name': instance.first_name,
            'last_name': instance.last_name,
            'password': instance.password,
            'tipo': instance.tipo,
            'descripcion_tipo': tipo ,
            'foto': instance.foto,
            'telefono': instance.telefono,
            'carrera': instance.carrera,
            'perfil': instance.perfil

        }


class Asignatura_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = '__all__'



class Asistencia_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id' : instance.id,
            'fecha': instance.fecha_clase,
            'id_alumno': instance.alumno.id,
            'nombre_aLumno': f'{instance.alumno.first_name} {instance.alumno.last_name}',
            'id_asignatura': instance.asignatura.id,
            'nombre_asignatura': instance.asignatura.nombre_asignatura,
            'seccion_asignatura': instance.asignatura.seccion,
            'id_profesor': instance.asignatura.profesor.id,
            'id_profesor': f'{instance.asignatura.profesor.first_name} {instance.asignatura.profesor.last_name}',  
        }
