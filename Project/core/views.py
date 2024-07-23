from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm 

# Create your views here.
def home(request):
    return render(request, 'base.html')

def login(request):
    
    '''
    Generate login form.
    Authenticate user.
    Login if authentic else add error
    
    '''
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        #Validate form
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            #Authenticate user
            user = authenticate(request, username=username, password=password)
            
            if user is not None:          
                auth_login(request, user)
                return redirect('/')
            
            else:
                #invalid user 
                form.add_error(None, "Invalid username or password.")
                return render(request, 'login.html', {'form':form})
                
    form = LoginForm()  
    return render(request, 'login.html', {'form':form})


def register(request):
    
    """
    Generates registration form.
    Performs validation of form inputs.
    Creates new user if valid.

    """        
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data['name']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            #Create a new user
            User.objects.create_user(username=username, password=password, first_name = name)
            
            return redirect('login')
        
        else:
            #return with form containing errors
            return render(request, 'register.html', {'form': form})
    
    #Create, then return form
    form = RegisterForm()
    return render(request, 'register.html', {'form':form})

def logout(request):
    auth_logout(request)
    return redirect('/')