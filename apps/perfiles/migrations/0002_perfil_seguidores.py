# Generated by Django 2.2.1 on 2019-06-02 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='seguidores',
            field=models.IntegerField(default=0),
        ),
    ]
