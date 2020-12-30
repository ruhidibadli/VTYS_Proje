# Generated by Django 3.1.4 on 2020-12-28 12:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('supermarket', '0002_delete_deneme'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beverages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.CharField(blank=True, default=0.0, max_length=150, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.BooleanField(blank=True, default=False)),
                ('is_empty', models.BooleanField(blank=True, default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=25)),
                ('number_of_carts', models.IntegerField(blank=True, default=0, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Groceries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='HouseHold',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Packaged_Foods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Personal_Care',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supermarket.cart')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supermarket.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Customer_Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supermarket.customer')),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supermarket.location')),
            ],
        ),
        migrations.CreateModel(
            name='Customer_Carts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supermarket.cart')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supermarket.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Cart_Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beverages_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='supermarket.beverages')),
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supermarket.cart')),
                ('groceries_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='supermarket.groceries')),
                ('household_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='supermarket.household')),
                ('packaged_foods_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='supermarket.packaged_foods')),
                ('personal_care_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='supermarket.personal_care')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='tags',
            field=models.ManyToManyField(to='supermarket.Tags'),
        ),
    ]