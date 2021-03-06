# Generated by Django 2.2.2 on 2020-04-01 21:47

from django.db import migrations


def crear_informacion_deleted(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    InformacionUsuario = apps.get_model('enunciados', 'InformacionUsuario')
    user = User.objects.get(username='Eliminado')
    InformacionUsuario.objects.create(usuario=user)


def eliminar_informacion_deleted(apps, schema_editor):
    InformacionUsuario = apps.get_model('auth', 'InformacionUsuario')
    InformacionUsuario.objects.get(usuario__username='Eliminado').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('enunciados', '0026_auto_20200116_2050'),
    ]

    operations = [
        migrations.RunPython(crear_informacion_deleted, eliminar_informacion_deleted)
    ]
