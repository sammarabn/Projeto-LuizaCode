# Generated by Django 3.2.7 on 2021-09-25 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_produto_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='categoria',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='app.categoria'),
        ),
    ]
