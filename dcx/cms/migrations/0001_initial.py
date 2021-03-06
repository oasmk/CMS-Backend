# Generated by Django 3.0.4 on 2021-02-28 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('contact_no', models.CharField(blank=True, max_length=14, null=True)),
                ('email_id', models.EmailField(blank=True, max_length=254, null=True)),
                ('message', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('image', models.FileField(upload_to='files/projects/')),
                ('on_display', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('designation', models.CharField(max_length=150)),
                ('testimonial', models.TextField()),
                ('image', models.FileField(upload_to='files/testimonials')),
                ('on_display', models.BooleanField(default=True)),
            ],
        ),
    ]
