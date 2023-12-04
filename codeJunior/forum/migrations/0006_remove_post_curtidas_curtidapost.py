# Generated by Django 4.2.4 on 2023-12-03 03:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0006_pessoa_emblemasganhos'),
        ('forum', '0005_alter_post_conteudo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='curtidas',
        ),
        migrations.CreateModel(
            name='CurtidaPost',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('dataCadastro', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data de Cadastro')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.post', verbose_name='Post')),
                ('quemCurtiu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.perfil', verbose_name='Perfil')),
            ],
            options={
                'verbose_name': 'Curtida Post',
                'verbose_name_plural': 'Curtidas Posts',
            },
        ),
    ]
