# Generated by Django 2.1.2 on 2018-10-30 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20181030_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interns',
            name='position',
            field=models.CharField(choices=[('Intern', 'INTERN'), ('Software developer', 'SOFTWARE DEVELOPER'), ('Founder', 'FOUNDER')], default='Intern', max_length=30),
        ),
    ]
