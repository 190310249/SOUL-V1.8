# Generated by Django 3.2.3 on 2022-01-09 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_home_testimonials_verification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home_testimonials',
            name='verification',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Not Accepted', 'Not Accepted')], default='Not Accepted', max_length=50),
        ),
    ]
