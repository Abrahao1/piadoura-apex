# Generated by Django 3.0.8 on 2020-08-04 22:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import pessoa.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='piadouro/imagens/')),
                ('telefone', models.CharField(max_length=20)),
                ('estado_civil', models.CharField(choices=[('s', 'Solteiro'), ('n', 'Namorando'), ('no', 'Noivado'), ('c', 'Casado'), ('v', 'Viuvo'), ('p', 'Piranhage')], max_length=2)),
                ('data_nascimento', models.DateField(validators=[pessoa.models.validador_idade])),
                ('estado', models.CharField(choices=[('rs', 'Rio Grande do Sul'), ('sc', 'Santa catarina'), ('pr', 'Paraná')], max_length=2)),
                ('cidade', models.CharField(max_length=64)),
                ('desempregado', models.BooleanField()),
                ('seguindo', models.ManyToManyField(blank=True, null=True, related_name='seguidores', to='pessoa.Perfil')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]