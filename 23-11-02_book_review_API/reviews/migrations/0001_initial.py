# Generated by Django 4.2.7 on 2023-11-02 13:03

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.TextField()),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1, message='Der Wert muss mindestens 1 sein!'), django.core.validators.MaxValueValidator(5, message='Der Wert darf höchstens 5 sein!')])),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.book')),
            ],
        ),
    ]