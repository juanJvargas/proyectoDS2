# Generated by Django 2.0.4 on 2018-06-10 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appprincipal', '0008_auto_20180526_0914'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreRequisito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Previo', models.ManyToManyField(related_name='prerequisito_requests_created', to='appprincipal.Curso')),
                ('curso', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='appprincipal.Curso')),
            ],
        ),
    ]
