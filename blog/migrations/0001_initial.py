# Generated by Django 3.2.8 on 2021-10-21 11:06

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_no', models.CharField(default='N/A', max_length=10485760)),
                ('date', models.CharField(default='N/A', max_length=1000)),
                ('time', models.CharField(default='N/A', max_length=1000)),
                ('name_of_hospital', models.CharField(default='N/A', max_length=1000)),
                ('contact_person', models.CharField(default='N/A', max_length=1000)),
                ('contact_number', models.CharField(default='N/A', max_length=1000)),
                ('product_description', models.TextField(default='N/A', max_length=10000)),
                ('brand', models.CharField(default='N/A', max_length=1000)),
                ('model', models.CharField(default='N/A', max_length=1000)),
                ('s_n', models.CharField(default='N/A', max_length=1000)),
                ('complaint', models.CharField(default='N/A', max_length=1000)),
                ('referred_by', models.CharField(default='N/A', max_length=1000)),
                ('receiver_name', models.CharField(default='N/A', max_length=1000)),
                ('receive_date', models.CharField(default='N/A', max_length=1000)),
                ('receive_time', models.CharField(default='N/A', max_length=1000)),
                ('assign_by', models.CharField(default='N/A', max_length=1000)),
                ('assign_date', models.CharField(default='N/A', max_length=1000)),
                ('assign_time', models.CharField(default='N/A', max_length=1000)),
                ('expected_duration', models.CharField(default='N/A', max_length=1000)),
                ('assign_to', models.CharField(default='N/A', max_length=1000)),
                ('assign_order_remark', models.CharField(default='N/A', max_length=1000)),
                ('open_close', models.CharField(default='N/A', max_length=1000)),
                ('service_report_doc_no', models.CharField(default='N/A', max_length=1000)),
                ('inspection', models.CharField(default='N/A', max_length=1000)),
                ('repair_description', models.TextField(default='N/A', max_length=10000)),
                ('spare_part_request_doc_no', models.CharField(default='N/A', max_length=1000)),
                ('warranty_card_no', models.CharField(default='N/A', max_length=1000)),
                ('service_start_date', models.CharField(default='N/A', max_length=1000)),
                ('service_finished_date', models.CharField(default='N/A', max_length=1000)),
                ('service_total_time', models.CharField(default='N/A', max_length=1000)),
                ('service_remark', models.CharField(default='N/A', max_length=1000)),
                ('recorded_by', models.CharField(default='N/A', max_length=1000)),
                ('date_posted', models.DateTimeField(default=datetime.datetime(2021, 10, 21, 11, 6, 18, 748539, tzinfo=utc))),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(default='N/A', max_length=10485760)),
                ('product_description', models.TextField(default='N/A', max_length=10000)),
                ('brand', models.CharField(default='N/A', max_length=1000)),
                ('model', models.CharField(default='N/A', max_length=1000)),
                ('s_n', models.CharField(default='N/A', max_length=1000)),
                ('hospital', models.CharField(default='N/A', max_length=1000)),
                ('city', models.CharField(default='N/A', max_length=1000)),
                ('installation_service_contract_doc_no', models.CharField(default='N/A', max_length=1000)),
                ('installed_service_contract_date', models.CharField(default='N/A', max_length=1000)),
                ('service_contract_package', models.CharField(default='N/A', max_length=1000)),
                ('first_date', models.CharField(default='N/A', max_length=1000)),
                ('first_doc_no', models.CharField(default='N/A', max_length=1000)),
                ('first_provider', models.CharField(default='N/A', max_length=1000)),
                ('first_remark', models.CharField(default='N/A', max_length=1000)),
                ('second_date', models.CharField(default='N/A', max_length=1000)),
                ('second_doc_no', models.CharField(default='N/A', max_length=1000)),
                ('second_provider', models.CharField(default='N/A', max_length=1000)),
                ('second_remark', models.CharField(default='N/A', max_length=1000)),
                ('third_date', models.CharField(default='N/A', max_length=1000)),
                ('third_doc_no', models.CharField(default='N/A', max_length=1000)),
                ('third_provider', models.CharField(default='N/A', max_length=1000)),
                ('third_remark', models.CharField(default='N/A', max_length=1000)),
                ('fourth_date', models.CharField(default='N/A', max_length=1000)),
                ('fourth_doc_no', models.CharField(default='N/A', max_length=1000)),
                ('fourth_provider', models.CharField(default='N/A', max_length=1000)),
                ('fourth_remark', models.CharField(default='N/A', max_length=1000)),
                ('date_posted', models.DateTimeField(default=datetime.datetime(2021, 10, 21, 11, 6, 18, 748539, tzinfo=utc))),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InstallationRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_no', models.CharField(default='N/A', max_length=10485760)),
                ('date', models.CharField(default='N/A', max_length=1000)),
                ('time', models.CharField(default='N/A', max_length=1000)),
                ('name_of_hospital', models.CharField(default='N/A', max_length=1000)),
                ('address', models.CharField(default='N/A', max_length=1000)),
                ('contact_person', models.CharField(default='N/A', max_length=1000)),
                ('contact_number', models.CharField(default='N/A', max_length=1000)),
                ('product_description', models.TextField(default='N/A', max_length=10000)),
                ('brand', models.CharField(default='N/A', max_length=1000)),
                ('model', models.CharField(default='N/A', max_length=1000)),
                ('s_n', models.CharField(default='N/A', max_length=1000)),
                ('referred_by', models.CharField(default='N/A', max_length=1000)),
                ('receiver_name', models.CharField(default='N/A', max_length=1000)),
                ('receive_date', models.CharField(default='N/A', max_length=1000)),
                ('receive_time', models.CharField(default='N/A', max_length=1000)),
                ('assign_by', models.CharField(default='N/A', max_length=1000)),
                ('assign_date', models.CharField(default='N/A', max_length=1000)),
                ('assign_time', models.CharField(default='N/A', max_length=1000)),
                ('expected_duration', models.CharField(default='N/A', max_length=1000)),
                ('assign_to', models.CharField(default='N/A', max_length=1000)),
                ('assign_remark', models.CharField(default='N/A', max_length=1000)),
                ('installation_doc_no', models.CharField(default='N/A', max_length=1000)),
                ('ref_inovice_contract_no', models.CharField(default='N/A', max_length=1000)),
                ('installed_date', models.CharField(default='N/A', max_length=1000)),
                ('installed_by', models.CharField(default='N/A', max_length=1000)),
                ('service_contact_package', models.CharField(default='N/A', max_length=1000)),
                ('warranty_card_no', models.CharField(default='N/A', max_length=1000)),
                ('machine_warranty_expiry_date', models.CharField(default='N/A', max_length=1000)),
                ('service_warranty_expiry_date', models.CharField(default='N/A', max_length=1000)),
                ('installation_duration', models.CharField(default='N/A', max_length=1000)),
                ('record_by', models.CharField(default='N/A', max_length=1000)),
                ('installation_remark', models.CharField(default='N/A', max_length=1000)),
                ('date_posted', models.DateTimeField(default=datetime.datetime(2021, 10, 21, 11, 6, 18, 748539, tzinfo=utc))),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]