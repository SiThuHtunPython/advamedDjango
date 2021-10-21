from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Maintenance(models.Model):
    no = models.CharField(max_length=10485760, default="N/A")
    product_description = models.TextField(max_length=10000, default="N/A")
    brand = models.CharField(max_length=1000, default="N/A")
    model = models.CharField(max_length=1000, default="N/A")
    s_n = models.CharField(max_length=1000, default="N/A")
    hospital = models.CharField(max_length=1000, default="N/A")
    city = models.CharField(max_length=1000, default="N/A")
    installation_service_contract_doc_no = models.CharField(max_length=1000, default="N/A")
    installed_service_contract_date = models.CharField(max_length=1000, default="N/A")
    service_contract_package = models.CharField(max_length=1000, default="N/A")
    first_date = models.CharField(max_length=1000, default="N/A")
    first_doc_no = models.CharField(max_length=1000, default="N/A")
    first_provider = models.CharField(max_length=1000, default="N/A")
    first_remark = models.CharField(max_length=1000, default="N/A")
    second_date = models.CharField(max_length=1000, default="N/A")
    second_doc_no = models.CharField(max_length=1000, default="N/A")
    second_provider = models.CharField(max_length=1000, default="N/A")
    second_remark = models.CharField(max_length=1000, default="N/A")
    third_date = models.CharField(max_length=1000, default="N/A")
    third_doc_no = models.CharField(max_length=1000, default="N/A")
    third_provider = models.CharField(max_length=1000, default="N/A")
    third_remark = models.CharField(max_length=1000, default="N/A")
    fourth_date = models.CharField(max_length=1000, default="N/A")
    fourth_doc_no = models.CharField(max_length=1000, default="N/A")
    fourth_provider = models.CharField(max_length=1000, default="N/A")
    fourth_remark = models.CharField(max_length=1000, default="N/A")
    date_posted = models.DateTimeField(default=timezone.now())
    author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.no

    def get_absolute_url(self):
        return reverse('maintenance_data-detail', kwargs={'pk': self.pk})


class ServiceRecord(models.Model):
    case_no = models.CharField(max_length=10485760, default="N/A")
    date = models.CharField(max_length=1000, default="N/A")
    time = models.CharField(max_length=1000, default="N/A")
    name_of_hospital = models.CharField(max_length=1000, default="N/A")
    contact_person = models.CharField(max_length=1000, default="N/A")
    contact_number = models.CharField(max_length=1000, default="N/A")
    product_description = models.TextField(max_length=10000, default="N/A")
    brand = models.CharField(max_length=1000, default="N/A")
    model = models.CharField(max_length=1000, default="N/A")
    s_n = models.CharField(max_length=1000, default="N/A")
    complaint = models.CharField(max_length=1000, default="N/A")
    referred_by = models.CharField(max_length=1000, default="N/A")
    receiver_name = models.CharField(max_length=1000, default="N/A")
    receive_date = models.CharField(max_length=1000, default="N/A")
    receive_time = models.CharField(max_length=1000, default="N/A")
    assign_by = models.CharField(max_length=1000, default="N/A")
    assign_date = models.CharField(max_length=1000, default="N/A")
    assign_time = models.CharField(max_length=1000, default="N/A")
    expected_duration = models.CharField(max_length=1000, default="N/A")
    assign_to = models.CharField(max_length=1000, default="N/A")
    assign_order_remark = models.CharField(max_length=1000, default="N/A")
    open_close = models.CharField(max_length=1000, default="N/A")
    service_report_doc_no = models.CharField(max_length=1000, default="N/A")
    inspection = models.CharField(max_length=1000, default="N/A")
    repair_description = models.TextField(max_length=10000, default="N/A")
    spare_part_request_doc_no = models.CharField(max_length=1000, default="N/A")
    warranty_card_no = models.CharField(max_length=1000, default="N/A")
    service_start_date = models.CharField(max_length=1000, default="N/A")
    service_finished_date = models.CharField(max_length=1000, default="N/A")
    service_total_time = models.CharField(max_length=1000, default="N/A")
    service_remark = models.CharField(max_length=1000, default="N/A")
    recorded_by = models.CharField(max_length=1000, default="N/A")
    date_posted = models.DateTimeField(default=timezone.now())
    author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.case_no

    def get_absolute_url(self):
        return reverse('service_record_data-detail', kwargs={'pk': self.pk})


class InstallationRecord(models.Model):
    case_no = models.CharField(max_length=10485760, default="N/A")
    date = models.CharField(max_length=1000, default="N/A")
    time = models.CharField(max_length=1000, default="N/A")
    name_of_hospital = models.CharField(max_length=1000, default="N/A")
    address = models.CharField(max_length=1000, default="N/A")
    contact_person = models.CharField(max_length=1000, default="N/A")
    contact_number = models.CharField(max_length=1000, default="N/A")
    product_description = models.TextField(max_length=10000, default="N/A")
    brand = models.CharField(max_length=1000, default="N/A")
    model = models.CharField(max_length=1000, default="N/A")
    s_n = models.CharField(max_length=1000, default="N/A")
    referred_by = models.CharField(max_length=1000, default="N/A")
    receiver_name = models.CharField(max_length=1000, default="N/A")
    receive_date = models.CharField(max_length=1000, default="N/A")
    receive_time = models.CharField(max_length=1000, default="N/A")
    assign_by = models.CharField(max_length=1000, default="N/A")
    assign_date = models.CharField(max_length=1000, default="N/A")
    assign_time = models.CharField(max_length=1000, default="N/A")
    expected_duration = models.CharField(max_length=1000, default="N/A")
    assign_to = models.CharField(max_length=1000, default="N/A")
    assign_remark = models.CharField(max_length=1000, default="N/A")
    installation_doc_no = models.CharField(max_length=1000, default="N/A")
    ref_inovice_contract_no = models.CharField(max_length=1000, default="N/A")
    installed_date = models.CharField(max_length=1000, default="N/A")
    installed_by = models.CharField(max_length=1000, default="N/A")
    service_contact_package = models.CharField(max_length=1000, default="N/A")
    warranty_card_no = models.CharField(max_length=1000, default="N/A")
    machine_warranty_expiry_date = models.CharField(max_length=1000, default="N/A")
    service_warranty_expiry_date = models.CharField(max_length=1000, default="N/A")
    installation_duration = models.CharField(max_length=1000, default="N/A")
    record_by = models.CharField(max_length=1000, default="N/A")
    installation_remark = models.CharField(max_length=1000, default="N/A")
    date_posted = models.DateTimeField(default=timezone.now())
    author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.case_no

    def get_absolute_url(self):
        return reverse('installation_record_data-detail', kwargs={'pk': self.pk})

