# Generated by Django 4.2.7 on 2023-12-20 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0005_callbackdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessToCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ResultCode', models.DecimalField(decimal_places=2, max_digits=9)),
                ('ResultDesc', models.CharField(max_length=255)),
                ('ConversationID', models.CharField(max_length=255)),
                ('Amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('MpesaReceiptNumber', models.CharField(max_length=255)),
                ('PhoneNumber', models.CharField(max_length=30)),
                ('TransactionDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
