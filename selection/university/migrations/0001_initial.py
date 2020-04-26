# Generated by Django 2.2.1 on 2019-05-10 09:13

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
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Факультет',
                'verbose_name_plural': 'Факультеты',
            },
        ),
        migrations.CreateModel(
            name='Special',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('number_budget_places', models.PositiveIntegerField(verbose_name='Количество бюджетных мест')),
                ('number_paid_places', models.PositiveIntegerField(verbose_name='Количество платных мест')),
                ('number_target_places', models.PositiveIntegerField(verbose_name='Количество целевых мест')),
                ('cost', models.FloatField(verbose_name='Плата за обучение')),
                ('is_stipend', models.BooleanField(verbose_name='Наличие стипендии')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.Faculty', verbose_name='Факультет')),
            ],
            options={
                'verbose_name': 'Специальность',
                'verbose_name_plural': 'Специальсноти',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предметы',
            },
        ),
        migrations.CreateModel(
            name='Statement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_type', models.CharField(choices=[('budget', 'На бюджетной основе'), ('commerce', 'На коммерческой основе')], max_length=200, verbose_name='Тип оплаты')),
                ('learning_type', models.CharField(choices=[('internal', 'Очная'), ('part_time', 'Очно-заочная (вечерняя)'), ('distance ', 'Заочная')], max_length=200, verbose_name='Форма обучения')),
                ('status', models.CharField(choices=[('verification_wait', 'Ожидает подтверждения'), ('verification_success', 'Заявление принято'), ('verification_denied', 'Заявление отклонено')], default='verification_wait', max_length=200, verbose_name='Статус')),
                ('entrant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Абитуриент')),
                ('special', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.Special', verbose_name='Специальность')),
            ],
            options={
                'verbose_name': 'Заявление',
                'verbose_name_plural': 'Заявления',
            },
        ),
        migrations.AddField(
            model_name='special',
            name='subjects',
            field=models.ManyToManyField(blank=True, to='university.Subject', verbose_name='Предметы'),
        ),
    ]
