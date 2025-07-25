# Generated by Django 5.2.3 on 2025-06-12 19:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rewards', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(null=True)),
                ('height', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=2)),
                ('points', models.IntegerField(default=0)),
                ('kind', models.CharField(choices=[('VG', 'Vegetarian'), ('NVG', 'Non-Vegetarian')], default='NVG', max_length=5)),
                ('achievements', models.ManyToManyField(blank=True, to='rewards.achievement')),
                ('badges', models.ManyToManyField(blank=True, to='rewards.badge')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
