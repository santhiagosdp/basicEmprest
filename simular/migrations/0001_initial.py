# Generated by Django 3.0.7 on 2020-06-25 00:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='simulacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=200)),
                ('valor', models.CharField(max_length=200)),
                ('parcelas', models.IntegerField()),
                ('valorfinal', models.IntegerField()),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
