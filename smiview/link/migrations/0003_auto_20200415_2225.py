# Generated by Django 2.2 on 2020-04-15 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0002_auto_20200414_1728'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name': 'Служба', 'verbose_name_plural': 'Службы'},
        ),
        migrations.AlterModelOptions(
            name='keyword',
            options={'verbose_name': 'Тэг', 'verbose_name_plural': 'Тэги'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Публикация', 'verbose_name_plural': 'Публикации'},
        ),
        migrations.AlterModelOptions(
            name='newstype',
            options={'verbose_name': 'Категория новостей', 'verbose_name_plural': 'Категории новостей'},
        ),
        migrations.AlterModelOptions(
            name='smi',
            options={'verbose_name': 'СМИ', 'verbose_name_plural': 'СМИ'},
        ),
        migrations.AlterModelOptions(
            name='typesmi',
            options={'verbose_name': 'Тип СМИ', 'verbose_name_plural': 'Типы СМИ'},
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название службы'),
        ),
        migrations.AlterField(
            model_name='keyword',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Ключевое слово'),
        ),
        migrations.AlterField(
            model_name='news',
            name='age',
            field=models.BooleanField(default=False, verbose_name='Дети'),
        ),
        migrations.AlterField(
            model_name='news',
            name='departments',
            field=models.ManyToManyField(to='link.Department', verbose_name='Служба'),
        ),
        migrations.AlterField(
            model_name='news',
            name='keywords',
            field=models.ManyToManyField(to='link.KeyWord', verbose_name='Ключевые слова'),
        ),
        migrations.AlterField(
            model_name='news',
            name='name',
            field=models.CharField(max_length=280, verbose_name='Новость'),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_type', to='link.NewsType', verbose_name='Категория новостей'),
        ),
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateField(verbose_name='Дата новости'),
        ),
        migrations.AlterField(
            model_name='news',
            name='smi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='smi', to='link.Smi', verbose_name='СМИ'),
        ),
        migrations.AlterField(
            model_name='news',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='link'),
        ),
        migrations.AlterField(
            model_name='newstype',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Категория новостей'),
        ),
        migrations.AlterField(
            model_name='smi',
            name='name',
            field=models.CharField(max_length=200, verbose_name='СМИ'),
        ),
        migrations.AlterField(
            model_name='smi',
            name='type_smi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type_smi', to='link.TypeSmi', verbose_name='Тип СМИ'),
        ),
        migrations.AlterField(
            model_name='smi',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='typesmi',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Тип СМИ'),
        ),
    ]
