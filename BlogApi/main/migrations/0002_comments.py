# Generated by Django 4.2.4 on 2023-09-01 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=300)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.post')),
            ],
        ),
    ]