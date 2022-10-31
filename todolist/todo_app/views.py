from turtle import title
from django.shortcuts import render,HttpResponseRedirect, HttpResponse, redirect
from .forms import AddListForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *

# Create your views here.
# def index(request):
#     return render(request, 'todo_app/index.html')

def first(request):
    if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST or None)
            if fm.is_valid():
                username = fm.cleaned_data['username']
                password = fm.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, f"You are now logged in as {username}.")
                    return redirect('home')
            else:
                messages.error(request, 'Invalid username or password !!')
                return redirect('first')
    else:   
        fm = AuthenticationForm()
        return render(request, 'todo_app/first.html', {'form':fm})

def registerfirst(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username aalreay exist! Please try some other username")
            return redirect('registerfirst')

        # if User.objects.filter(email=email):
        #     messages.error(request, "Email already registered")

        if len(username)>10:
            messages.error(request, "Username must be unser 10 character")

        if pass1!=pass2:
            messages.error(request, "Password didn't match!")

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "your account has been successfully created.")
        return redirect('registerfirst')
    return render(request, 'todo_app/registerfirst.html')

# def user_login(request):
#     if request.method == "POST":
#             fm = AuthenticationForm(request=request, data=request.POST or None)
#             if fm.is_valid():
#                 username = fm.cleaned_data['username']
#                 password = fm.cleaned_data['password']
#                 user = authenticate(username=username, password=password)
#                 if user is not None:
#                     login(request, user)
#                     messages.success(request, f"You are now logged in as {username}.")
#                     return redirect('home')
#             else:
#                 return HttpResponse('invalid')
#     else:    
#         fm = AuthenticationForm()
#         return render(request, 'todo_app/login.html', {'form':fm})

# def register(request):
#     if request.method == 'POST':
#         fm = SignUpForm(request.POST)
#         if fm.is_valid():
#             messages.success(request, 'Account Created Sucessfully !!')
#             fm.save()
#     else:
#         fm = SignUpForm()
#     return render(request, 'todo_app/register.html',{'form':fm})

def user_logout(request):
    logout(request)
    messages.success(request, "You have successfully logged out.") 
    return redirect('first')

def profile(request):
    
    return render(request, 'todo_app/profile.html')

# def home(request, id):
#     if request.session.has_key('session_username'):
#         list = User.objects.get(id=id)
#         context = {
#             'list': list,
#         }
#         return render(request, 'todo_app/home.html', context)
#     return redirect('login')


def home(request):
    lists = Task.objects.filter(user=request.user)
    return render(request, 'todo_app/home.html', {'lists':lists})

def addlist(request):
    if request.method == 'POST':
        fm = AddListForm(request.POST)
        if fm.is_valid():
            form_obj = fm.save(commit=False)
            form_obj.user = request.user
            fm.save()
            return redirect('home')
            
    else:
        fm = AddListForm()
    return render(request, 'todo_app/add_list.html', {'form':fm})

def edit(request, id):
    task = Task.objects.get(id=id)
    form = AddListForm(instance=task)
    if request.method == "POST":
        form = AddListForm(request.POST, instance=task)
        if form.is_valid:
            form.save()
            return redirect('home')

    return render(request, 'todo_app/edit.html', {'form':form})

def delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('home')



# def addlist(request):
#     if(request.session.has_key('username')):
#         template = "todo_app/add_list.html"
#         create_form = AddListForm()
#         context = {"form": create_form}
#         if request.method == "POST":
#             list = AddList()
#             list.title = request.POST.get("title")
#             list.description = request.POST.get("description")
#             list.date = request.POST.get("date")

#             user = User.objects.get(username=request.session.get("username"))
#             list.user = user
#             list.save()
#             return redirect("home")
#         return render(request, template, context)
#     return redirect("login")    

        # context = {"form": create_form}
        #     username = request.session['username']
        #     data = Enquiry.objects.filter(service=request.session['service'])
