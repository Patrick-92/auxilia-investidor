# Generated by Django 3.1.3 on 2020-11-28 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carteira',
            name='ativos',
        ),
        migrations.AddField(
            model_name='ativo',
            name='carteira',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='core.carteira'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ativo',
            name='lim_inf',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AddField(
            model_name='ativo',
            name='lim_sup',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='ativo',
            name='preco',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7),
        ),
    ]
