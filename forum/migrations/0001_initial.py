# Generated by Django 4.2.4 on 2024-11-02 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255, verbose_name='Nome da Área')),
                ('descricao', models.TextField(blank=True, max_length=500, null=True, verbose_name='Descrição da Área')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
            ],
            options={
                'verbose_name': 'Área',
                'verbose_name_plural': 'Áreas',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('conteudo', models.TextField(max_length=500000, verbose_name='Conteúdo do Post')),
                ('index', models.BooleanField(default=False, verbose_name='É o Primeiro Post?')),
                ('dataCadastro', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data de Cadastro')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('quemPostou', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.perfil', verbose_name='perfil')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='Secao',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255, verbose_name='Nome da Seção')),
                ('descricao', models.TextField(blank=True, max_length=500, null=True, verbose_name='Descrição da Seção')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.area', verbose_name='Area')),
            ],
            options={
                'verbose_name': 'Seção',
                'verbose_name_plural': 'Seções',
            },
        ),
        migrations.CreateModel(
            name='SubSecao',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255, verbose_name='Nome da Subseção')),
                ('descricao', models.TextField(blank=True, max_length=500, null=True, verbose_name='Descrição da Subseção')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('secao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.secao', verbose_name='secao')),
            ],
            options={
                'verbose_name': 'Subseção',
                'verbose_name_plural': 'Subseções',
            },
        ),
        migrations.CreateModel(
            name='Topico',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255, verbose_name='Nome da Tópico')),
                ('dataCadastro', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data de Cadastro')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('secao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.secao', verbose_name='secao')),
                ('subsecao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='forum.subsecao', verbose_name='subsecao')),
            ],
            options={
                'verbose_name': 'Tópico',
                'verbose_name_plural': 'Tópicos',
            },
        ),
        migrations.CreateModel(
            name='RespostaPost',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('dataCadastro', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data de Cadastro')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='forum.post', verbose_name='Post')),
                ('resposta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resposta', to='forum.post', verbose_name='Resposta')),
            ],
            options={
                'verbose_name': 'Resposta Post',
                'verbose_name_plural': 'Respostas Posts',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='topico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.topico', verbose_name='topico'),
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
