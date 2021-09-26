# Generated by Django 3.2.7 on 2021-09-25 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_delete_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, unique=True)),
                ('lojaPertencente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.loja')),
            ],
        ),
    ]