# Generated by Django 2.0.4 on 2018-06-11 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appprincipal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndicadorEvaluacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('descripcion', models.TextField(blank=True, max_length=500)),
                ('indicador', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='appprincipal.Indicador')),
            ],
        ),
    ]