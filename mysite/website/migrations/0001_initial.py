# Generated by Django 4.1.6 on 2023-02-18 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('food', models.CharField(choices=[('Italian', 'Italian'), ('Mexican', 'Mexican'), ('Japanese', 'Japanese'), ('Greek', 'Greek'), ('German', 'German')], max_length=200, null=True)),
                ('payment', models.CharField(choices=[('Cash', 'Cash'), ('Card', 'Card')], max_length=200, null=True)),
                ('expectation', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'orders',
            },
        ),
    ]
