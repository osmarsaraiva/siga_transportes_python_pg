# Generated by Django 4.1.7 on 2023-11-19 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acertosviagens',
            name='fk_lancar_viagens',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.lancarviagens'),
        ),
    ]