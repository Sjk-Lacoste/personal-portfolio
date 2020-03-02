# Generated by Django 3.0.3 on 2020-03-02 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='projects/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='updated_on',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='skill',
            name='image',
            field=models.ImageField(upload_to='skills/'),
        ),
        migrations.AlterField(
            model_name='techstack',
            name='image',
            field=models.ImageField(upload_to='techstack/'),
        ),
    ]
