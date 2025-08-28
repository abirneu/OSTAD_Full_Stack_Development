from urllib import request
from django.shortcuts import render, HttpResponse, redirect
from .import models
from . import forms
from django.contrib import messages
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.
#Three types oḟform in django

#This is HTML form

#This is model form
@login_required
def create_student(request):
    if request.method == 'POST': #1. user post requesţkoreche
        form = forms.StudentForm(request.POST, request.FILES) #2. user post request capture korlam
        if form.is_valid(): #3. user input validation 
            form.save() #4. form er data save korlam
            messages.add_message(request, messages.SUCCESS, 'Student Created  successfully.')
            return redirect('home')
    else:
        form = forms.StudentForm() 
    return render( request, 'student/create_edit_student.html', {'form': form})

class CreateStudent(LoginRequiredMixin, CreateView):
    form_class = forms.StudentForm
    success_url = reverse_lazy('home')
    template_name = 'student/create_edit_student.html'

    def form_valid(self, form):
        student = form.save(commit=False)
        student.user = self.request.user
        student.save()
        messages.add_message(self.request, messages.SUCCESS, 'Student Created  successfully.')
        return super().form_valid(form)


def home(request):
    students = models.Student.objects.all()
    return render(request, 'student/index.html', {'students': students})
#student data updater er jonno
@login_required
def update_student(request, id):
    student = models.Student.objects.get(id=id) #collecting student info using id
    form = forms.StudentForm(instance=student) #student form er data fill up kora thakbe

    # form = forms.StudentForm() 
    if request.method == 'POST':
        form = forms.StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Student Updated  successfully.')

            return redirect('home')

    return render( request, 'student/create_edit_student.html', {'form': form , 'edit':True})

class UpdateStudentData( LoginRequiredMixin ,UpdateView):
    form_class = forms.StudentForm
    model = models.Student
    template_name = 'student/create_edit_student.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id' 
# student selete  er jonno
@login_required
def delete_student(request, id):
    student = models.Student.objects.get(id= id) #1. id=id wala student ke khuje ber korlam
    student.delete() #2. oi student object ke delete korlam
    messages.add_message(request, messages.SUCCESS, 'Student Deleted  successfully.')

    return redirect('home') #3. successfull hole take home page e redirect kore dew



#User sign up form
def signup(request):
    if request.method == 'POST':
        form = forms.SingUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Account Created  successfully.')
            return redirect('home')
    else:
        form = forms.SingUpForm()
    return render(request, 'student/auth_form.html', {'form':form} ) 


#User Login
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data= request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, 'Login successfully.')
                return redirect('home')
            else:
                messages.add_message(request, messages.SUCCESS, 'Invaild username/password')

    else:
        form = AuthenticationForm()
    return render(request, 'student/auth_form.html', {'form':form})

#User Logout
def user_logout(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'Logout Successfully')
    return redirect('home')

@login_required
def user_profile(request):
    students = models.Student.objects.filter(user = request.user) #all student er data dekha
    return render(request, 'student/profile.html', {'students': students})



