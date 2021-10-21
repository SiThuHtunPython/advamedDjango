from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from .models import Maintenance, ServiceRecord, InstallationRecord
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required



class ServiceRecordDataListView(LoginRequiredMixin, ListView):
    model = ServiceRecord
    template_name = 'blog/service_record.html'
    context_object_name = 'service_records'
    ordering = ['-date_posted']



#class MaintenanceDataListView(LoginRequiredMixin, ListView):
#    model = Maintenance
#    template_name = 'blog/home.html'
#    context_object_name = 'posts'
#    ordering = ['-date_posted']


@login_required
def MaintenanceDataListView(request):
    if request.user.is_staff:
        context = {
            'posts': Maintenance.objects.all()
        }
        return render(request, 'blog/home.html', context)
    else:
        if request.user.has_perm('blog.change_maintenance'):
            context = {
                'posts': Maintenance.objects.all()
            }
            return render(request, 'blog/home.html', context)
        else:
            context = {
                'service_records': ServiceRecord.objects.all()
            }
            return render(request, 'blog/service_record.html', context)


'''def MaintenanceDataDetailView(request):
    if request.object.user:
        return render(request, 'blog/maintenance_detail.html', Maintenance.objects.all())
    else:
        return render(request, 'blog/home.html')'''

class InstallationRecordDataDetailView(LoginRequiredMixin, DetailView):
    model = InstallationRecord


class ServiceRecordDataDetailView(LoginRequiredMixin, DetailView):
    model = ServiceRecord


class MaintenanceDataDetailView(LoginRequiredMixin, DetailView):
    model = Maintenance



class MaintenanceDataCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'blog.add_maintenance'
    model = Maintenance
    fields = ['no', 'product_description', 'brand', 'model', 's_n', 'hospital', 'city',
              'installation_service_contract_doc_no', 'installed_service_contract_date',
              'service_contract_package', 'first_date', 'first_doc_no', 'first_provider', 'first_remark',
              'second_date', 'second_doc_no', 'second_provider' ,'second_remark', 'third_date', 'third_doc_no',
              'third_provider', 'third_remark', 'fourth_date', 'fourth_doc_no', 'fourth_provider', 'fourth_remark']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)





class MaintenanceDataUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Maintenance
    fields = ['no', 'product_description', 'brand', 'model', 's_n', 'hospital', 'city',
              'installation_service_contract_doc_no', 'installed_service_contract_date',
              'service_contract_package', 'first_date', 'first_doc_no', 'first_provider', 'first_remark',
              'second_date', 'second_doc_no', 'second_provider' ,'second_remark', 'third_date', 'third_doc_no',
              'third_provider', 'third_remark', 'fourth_date', 'fourth_doc_no', 'fourth_provider', 'fourth_remark']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class MaintenanceDataDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Maintenance
    success_url = '/home'


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class UserMaintenanceDataListView(LoginRequiredMixin, ListView):
    model = Maintenance
    template_name = 'blog/user_maintenance_data.html'
    context_object_name = 'posts'


    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Maintenance.objects.filter(author=user).order_by('-date_posted')



class ServiceRecordDataCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'blog.add_servicerecord'
    model = ServiceRecord
    fields = ['case_no', 'date', 'time', 'name_of_hospital', 'contact_person', 'contact_number', 'product_description',
              'brand', 'model', 's_n', 'complaint', 'referred_by', 'receiver_name', 'receive_date', 'receive_time',
              'assign_by', 'assign_date', 'assign_time', 'expected_duration', 'assign_to', 'assign_order_remark', 'open_close']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class ServiceRecordDataUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'blog.change_servicerecord'
    model = ServiceRecord
    fields = ['service_report_doc_no', 'inspection', 'repair_description', 'spare_part_request_doc_no',
              'warranty_card_no', 'service_start_date', 'service_finished_date', 'service_total_time',
              'service_remark', 'recorded_by']

    def form_valid(self, form):
        return super().form_valid(form)



class ServiceRecordDataDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'blog.delete_servicerecord'
    model = ServiceRecord
    success_url = '/home'



class UserServiceRecordDataListView(LoginRequiredMixin, ListView):
    model = ServiceRecord
    template_name = 'blog/user_service_record_data.html'
    context_object_name = 'service_records'


    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return ServiceRecord.objects.filter(author=user).order_by('-date_posted')



#, 'installation_doc_no',
#'ref_inovice_contract_no', 'installed_date', 'installed_by', 'service_contact_package', 'warranty_card_no', 'machine_warranty_expiry_date',
#'service_warranty_expiry_date', 'installation_duration', 'record_by', 'installation_remark'

class InstallationServiceDataListView(LoginRequiredMixin, ListView):
    model = InstallationRecord
    template_name = 'blog/installation_record.html'
    context_object_name = 'installation_records'
    ordering = ['-date_posted']



class InstallationRecordDataCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'blog.add_installationrecord'
    model = InstallationRecord
    fields = ['case_no', 'date', 'time', 'name_of_hospital', 'address', 'contact_person', 'contact_number', 'product_description',
              'brand', 'model', 's_n', 'referred_by', 'receiver_name', 'receive_date', 'receive_time',
              'assign_by', 'assign_date', 'assign_time', 'expected_duration', 'assign_to', 'assign_remark']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class InstallationRecordDataUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'blog.change_installationrecord'
    model = InstallationRecord
    fields = ['installation_doc_no', 'ref_inovice_contract_no', 'installed_date', 'installed_by',
              'service_contact_package', 'warranty_card_no', 'machine_warranty_expiry_date', 'service_warranty_expiry_date',
              'installation_duration', 'record_by', 'installation_remark']

    def form_valid(self, form):
        return super().form_valid(form)



class InstallationRecordDataDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'blog.delete_installationrecord'
    model = InstallationRecord
    success_url = '/home'



class UserInstallationRecordDataListView(LoginRequiredMixin, ListView):
    model = InstallationRecord
    template_name = 'blog/user_installation_record_data.html'
    context_object_name = 'installation_records'


    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return InstallationRecord.objects.filter(author=user).order_by('-date_posted')



@login_required
def maintenance2(request):
    return render(request, 'blog/maintenance2.html')


@login_required
def add_record_maintenance(request):
    return render(request, 'blog/add_record_maintenance.html', {'title': 'Add Record'})
