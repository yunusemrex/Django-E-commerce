# Generated by Django 4.0.2 on 2022-02-24 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0004_alter_page_cover_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(choices=[('draft', 'Taslak'), ('published', 'Yayinlanmis'), ('deleted', 'Silindi')], default='draft', max_length=10)),
                ('cover_image', models.ImageField(null=True, upload_to='carousel')),
                ('createt_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='page',
            name='status',
            field=models.CharField(choices=[('draft', 'Taslak'), ('published', 'Yayinlanmis'), ('deleted', 'Silindi')], default='draft', max_length=12),
        ),
    ]
