# Generated by Django 3.1.3 on 2020-11-20 06:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ativo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_ativ', models.CharField(max_length=100)),
                ('sigla', models.CharField(max_length=7)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Investidor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='investidor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='historicoAtivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('adj_close', models.DecimalField(decimal_places=2, max_digits=7)),
                ('close', models.DecimalField(decimal_places=2, max_digits=7)),
                ('High', models.DecimalField(decimal_places=2, max_digits=7)),
                ('Low', models.DecimalField(decimal_places=2, max_digits=7)),
                ('Open', models.DecimalField(decimal_places=2, max_digits=7)),
                ('Volume', models.PositiveIntegerField()),
                ('ativo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.ativo')),
            ],
        ),
        migrations.CreateModel(
            name='Carteira',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cart', models.CharField(blank=True, max_length=100)),
                ('ativos', models.ManyToManyField(to='core.Ativo')),
                ('investidor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.investidor')),
            ],
        ),
    ]
