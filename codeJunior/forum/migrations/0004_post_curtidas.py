# Generated by Django 4.2.4 on 2023-10-17 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_post_datacadastro_respostapost_datacadastro_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='curtidas',
            field=models.IntegerField(default=0, verbose_name='Curtidas'),
        ),
    ]
