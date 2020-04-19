# Generated by Django 2.2.2 on 2019-12-28 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enunciados', '0014_enunciado_votos'),
    ]

    operations = [
        migrations.CreateModel(
            name='VotoEnunciado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positivo', models.BooleanField()),
                ('enunciado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enunciados.Enunciado')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enunciados.InformacionUsuario')),
            ],
        ),
        migrations.AddField(
            model_name='informacionusuario',
            name='votos_enunciados',
            field=models.ManyToManyField(through='enunciados.VotoEnunciado', to='enunciados.Enunciado'),
        ),
    ]