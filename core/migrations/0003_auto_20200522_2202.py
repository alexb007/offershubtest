# Generated by Django 3.0.6 on 2020-05-22 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200522_2024'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workspace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('synced', models.BooleanField(default=False, editable=False, verbose_name='Синхронизировано')),
                ('gid', models.CharField(editable=False, max_length=32, null=True, unique=True, verbose_name='GID')),
                ('name', models.CharField(max_length=512, verbose_name='Название задачи')),
            ],
            options={
                'verbose_name': 'Рабочее пространство',
                'verbose_name_plural': 'Рабочие пространства',
            },
        ),
        migrations.RemoveField(
            model_name='task',
            name='completed_by',
        ),
        migrations.AlterField(
            model_name='asanauser',
            name='gid',
            field=models.CharField(editable=False, max_length=32, null=True, unique=True, verbose_name='GID'),
        ),
        migrations.AlterField(
            model_name='asanauser',
            name='synced',
            field=models.BooleanField(default=False, editable=False, verbose_name='Синхронизировано'),
        ),
        migrations.AlterField(
            model_name='project',
            name='gid',
            field=models.CharField(editable=False, max_length=32, null=True, unique=True, verbose_name='GID'),
        ),
        migrations.AlterField(
            model_name='project',
            name='synced',
            field=models.BooleanField(default=False, editable=False, verbose_name='Синхронизировано'),
        ),
        migrations.AlterField(
            model_name='task',
            name='gid',
            field=models.CharField(editable=False, max_length=32, null=True, unique=True, verbose_name='GID'),
        ),
        migrations.AlterField(
            model_name='task',
            name='synced',
            field=models.BooleanField(default=False, editable=False, verbose_name='Синхронизировано'),
        ),
        migrations.AddField(
            model_name='project',
            name='workspace',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='core.Workspace', verbose_name='Рабочее пространство'),
        ),
    ]