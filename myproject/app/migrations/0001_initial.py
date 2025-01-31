# Generated by Django 5.0.2 on 2024-03-20 06:23

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="authtoken_token",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name="Invoice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("invoice_number", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="login",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("password", models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name="Register",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("cname", models.CharField(max_length=255)),
                ("address", models.CharField(max_length=255)),
                (
                    "gst",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        default="0.00",
                        max_digits=10,
                        verbose_name="GST",
                    ),
                ),
                ("contactno", models.CharField(max_length=12)),
                ("contactperson", models.CharField(max_length=12)),
                ("created_date", models.DateField(auto_now_add=True)),
                ("is_active", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="Trans",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("password", models.CharField(max_length=256)),
                ("cname", models.CharField(max_length=255)),
                ("address", models.CharField(max_length=128)),
                (
                    "gst",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        default="0.00",
                        max_digits=10,
                        verbose_name="GST",
                    ),
                ),
                ("contactno", models.CharField(max_length=225)),
                ("contactperson", models.CharField(max_length=255)),
                ("image", models.FileField(null=True, upload_to="upload")),
                ("created_date", models.DateField(auto_now_add=True)),
                ("is_active", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="Employee",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("password", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=255)),
                ("phone", models.CharField(max_length=255)),
                ("created_date", models.DateField(auto_now_add=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "registerId",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.register",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="register",
            name="transId",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app.trans",
            ),
        ),
        migrations.CreateModel(
            name="Truck",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("dname", models.CharField(max_length=255)),
                ("dcontact", models.CharField(max_length=255)),
                ("truckno", models.CharField(max_length=10)),
                ("oname", models.CharField(max_length=255)),
                ("ocontact", models.CharField(blank=True, max_length=12)),
                ("Ttype", models.CharField(max_length=255)),
                ("created_date", models.DateField(default=datetime.datetime.now)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "transId",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.trans",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Billing",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255, null=True)),
                ("address", models.CharField(max_length=128, null=True)),
                (
                    "gst",
                    models.DecimalField(blank=True, decimal_places=2, max_digits=10),
                ),
                ("invoice_number", models.CharField(max_length=20, null=True)),
                ("fy", models.CharField(max_length=20, null=True)),
                ("inv_no", models.CharField(max_length=20, null=True)),
                ("From", models.CharField(max_length=255, null=True)),
                ("To", models.CharField(max_length=255, null=True)),
                ("Lr_no", models.CharField(max_length=255, null=True)),
                ("Dsicriptions", models.CharField(max_length=255, null=True)),
                ("Qty_weight", models.CharField(max_length=255, null=True)),
                ("Rate", models.CharField(max_length=255, null=True)),
                ("Amount", models.CharField(max_length=255, null=True)),
                ("created_date", models.DateField(auto_now_add=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "truck",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.truck",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Worker",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("lname", models.CharField(max_length=255)),
                ("address", models.CharField(max_length=128)),
                ("contactno", models.CharField(max_length=255)),
                ("created_date", models.DateField(auto_now_add=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "transId",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.trans",
                    ),
                ),
            ],
        ),
    ]
