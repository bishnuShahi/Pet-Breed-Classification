from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm
from django.http import JsonResponse 
import requests
import logging

logger = logging.getLogger(__name__)


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


def classify_image(request):
    if request.method == 'POST':
        image_file = request.FILES.get('image')
        if not image_file:
            logger.error('No image file provided in the request')
            return JsonResponse({'error': 'No image file provided'}, status=400)

        files = {'file': image_file}  # Update the field name here

        try:
            # Send the image file to the FastAPI API
            response = requests.post('http://127.0.0.1:8001/predict', files=files)
            logger.info(f'FastAPI response status code: {response.status_code}')

            if response.status_code == 200:
                # Return the response from the FastAPI API
                return JsonResponse(response.json())
            else:
                logger.error(f'FastAPI API failed with status code: {response.status_code}')
                logger.error(f'FastAPI API response: {response.text}')
                return JsonResponse({'error': 'Failed to classify image'}, status=response.status_code)

        except requests.exceptions.RequestException as e:
            logger.error(f'Error sending request to FastAPI API: {e}')
            return JsonResponse({'error': 'Failed to classify image'}, status=500)

    logger.error('Invalid request method')
    return JsonResponse({'error': 'Invalid request method'}, status=405)


            
    