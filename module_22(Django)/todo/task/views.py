from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm


# Create your views here.
def task_list(request):
    if not request.user.is_authenticated:
        return redirect('login')
        
    status_filter = request.GET.get('status', 'all') # pending, completed
    category_filter = request.GET.get('category', 'all')
    task = Task.objects.filter(user = request.user)

    if status_filter != 'all':
        task = task.filter(is_completed=(status_filter=='completed'))

    if category_filter != 'all':
        task = task.filter(category = category_filter)

    completed_task = task.filter(is_completed = True)
    pending_task = task.filter(is_completed = False)

    return render(request, 'task_list.html',{
        'completed_task': completed_task,
        'pending_task':pending_task,
        'status_filter':status_filter,
        'category_filter': category_filter,

    })
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False) #user set kora hoy nia tai False
            task.user = request.user
            task.save()
            return redirect('task_create.html')
    else:
        form = TaskForm
    return redirect(request,'task_form.html', {'form':form})
@login_required
def task_detail(request,task_id):
    task = get_object_or_404(Task, id=task_id, user= request.user) # user login na korle task dekhte parbe na
    return render(request, 'task_detail.html', {'task':task})

@login_required
def task_delete(request,task_id):
    task = get_object_or_404(Task, id=task_id, user= request.user) # user login na korle task dekhte parbe na
    task.delete()
    return redirect('task_list.html')
@login_required
def task_mark_completed(request,task_id):
    task = get_object_or_404(Task, id=task_id, user= request.user) # user login na korle task dekhte parbe na
    task.is_completed = True
    task.save()
    return redirect('task_list')


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() #databse e user create hoye geche
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            print(username,password)
            user = authenticate(username = username, password = password)
            print(user)
            login(request, user)
            return redirect('task_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form':form})


def login_view(request): 
    form = LoginForm() 
    if request.method == 'POST': 
        form = LoginForm(request.POST) 
        if form.is_valid(): 
            username = form.cleaned_data['username'] 
            password = form.cleaned_data['password'] 
            user = authenticate(request, username=username, password=password) 
            if user is not None: 
                login(request, user) 
                return redirect('task_list') # Redirect to a success page 
            else: form.add_error(None, "Invalid username or password.") 

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')