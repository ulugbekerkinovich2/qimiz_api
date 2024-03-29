# Generated by Django 4.2 on 2023-04-29 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0002_about_text_en_about_title_en_comments_text_en_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qimiz_Dacha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('cost_title', models.CharField(blank=True, max_length=255, null=True)),
                ('rating', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'verbose_name_plural': 'Qimiz_Dacha',
            },
        ),
        migrations.AddField(
            model_name='dachakategory',
            name='name_en',
            field=models.CharField(default='kategoriya kitilmagan', max_length=512),
        ),
    ]
