# Generated by Django 3.2 on 2022-03-15 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cross_word', '0003_cross_wordsomething'),
    ]

    operations = [
        migrations.AddField(
            model_name='cross_wordsomething',
            name='crossword_level',
            field=models.IntegerField(default=-1),
        ),
    ]
