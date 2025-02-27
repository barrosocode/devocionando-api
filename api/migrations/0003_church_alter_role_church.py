# Generated by Django 5.1.6 on 2025-02-27 18:17

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_references_reference'),
    ]

    operations = [
        migrations.CreateModel(
            name='Church',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='role',
            name='church',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.church'),
        ),
    ]
