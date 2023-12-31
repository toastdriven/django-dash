# Generated by Django 4.2.7 on 2023-11-21 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('competitions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('url', models.URLField(blank=True, null=True)),
                ('description', models.TextField(blank=True, default='')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now=True, db_index=True)),
                ('competitions', models.ManyToManyField(related_name='sponsors', to='competitions.competition')),
            ],
        ),
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('place', models.CharField(choices=[['first', 'First'], ['second', 'Second'], ['third', 'Third'], ['participation', 'Participation']], db_index=True, default='first', max_length=16)),
                ('estimated_value', models.PositiveIntegerField(blank=True, default=0, help_text='This is an internal-only field, to help with prize allocations.')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now=True, db_index=True)),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prizes', to='competitions.competition')),
                ('sponsor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prizes', to='sponsors.sponsor')),
            ],
        ),
    ]
