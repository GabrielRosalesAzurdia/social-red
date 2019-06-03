# Generated by Django 2.2.1 on 2019-06-01 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('contenido', models.TextField()),
                ('fecha_publicacion', models.DateField()),
                ('autor', models.CharField(max_length=20)),
            ],
        ),
    ]