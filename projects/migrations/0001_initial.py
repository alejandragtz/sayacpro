# Generated by Django 2.2.6 on 2019-12-06 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeProject', models.CharField(blank=True, choices=[(None, 'Selecciona estado'), ('Interno', 'Interno'), ('Externo', 'Externo'), ('Convenio', 'Convenio'), ('UABC', 'UABC')], max_length=25, verbose_name=' Tipo de proyecto')),
                ('titleProject', models.CharField(blank=True, default='Proyecto', max_length=50, null=True, verbose_name='Título de proyecto')),
                ('announcementProject', models.CharField(blank=True, max_length=100, verbose_name=' Convocatoria (Si aplica)')),
                ('amountProject', models.CharField(blank=True, max_length=50, verbose_name='Monto')),
                ('responsableProject', models.CharField(blank=True, max_length=50, verbose_name='Responsable técnico')),
                ('partProject', models.TextField(blank=True, max_length=220, verbose_name='Participantes')),
                ('codeProject', models.CharField(blank=True, max_length=100, verbose_name='Clave')),
                ('vigenciaProject', models.DateField(verbose_name='Vigencia hasta')),
                ('stateProject', models.CharField(blank=True, choices=[(None, 'Selecciona estado'), ('Vigente', 'Vigente'), ('No vigente', 'No vigente'), ('Concluido', 'No Concluido')], max_length=25, verbose_name='Estado del proyecto')),
            ],
        ),
    ]
