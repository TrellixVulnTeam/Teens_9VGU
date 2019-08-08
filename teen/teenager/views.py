from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Student,Institution
from django.shortcuts import get_object_or_404 
from .forms import StudentCreateForm, InstitutionCreateForm
# Create your views here.
class HomePageView(TemplateView):
	template_name = 'teenager/home.html'


class StudentCreateView(CreateView):
	model = Student
	form_class = StudentCreateForm


class StudentDetailView(DetailView):
	model = Student
	context_object_name = 'teen'


class StudentListView(ListView):
	model = Student
	context_object_name = 'teens'

class StudentUpdateView(UpdateView):
	model = Student
	fields =['first_name', 'last_name', 'middle_name','date_of_birth','state_of_origin','email_address', 
			'image', 'phone_number', 'parent_full_name', 'parent_phone_number', 'address', ]
	template_name ='teenager/student_form.html'

class InstitutionCreateView(CreateView):
	model = Institution
	form_class = InstitutionCreateForm

	def form_valid(self,form):
		form.instance.student = Student.objects.get(id=self.kwargs.get('pk'))
		return super(InstitutionCreateView, self).form_valid(form)

class InstitutionListView(ListView):
	model = Institution
	template_name = 'teenager/student_list.html'
