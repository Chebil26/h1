# Generated by Django 4.0.4 on 2022-06-12 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_transfer_level_alter_transfer_orginal_uni'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='spe_choice',
            field=models.CharField(choices=[('MI', 'MI'), ('sport', 'sport'), ('eco', 'eco')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='orginal_uni',
            field=models.CharField(max_length=400, null=True),
        ),
    ]
