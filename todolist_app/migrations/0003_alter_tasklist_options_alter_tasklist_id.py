# Generated by Django 4.1.4 on 2022-12-26 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0002_tasklist_manager'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tasklist',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='tasklist',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
