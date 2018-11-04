# Generated by Django 2.1.2 on 2018-10-28 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conductor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=110)),
                ('identificacion', models.IntegerField()),
                ('correo', models.EmailField(max_length=254)),
                ('celular', models.IntegerField()),
            ],
            options={
                'ordering': ('identificacion',),
            },
        ),
    ]
